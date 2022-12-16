
# MIT License
#
# Copyright (c) 2021 Kevin L.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# How to run?
# This script runs standalone independent of the AnilistPython modules.
#
# To start retrieving a new database:
# $ python3 ./dbtool.py
# 
# If the run is stopped half-way, the program will auto detect the previous record
# retrieved and continue the run from there.

import sys
import os
import sqlite3
import time
from datetime import datetime

import __init__
from __init__ import Anilist, __version__

## NOTE: retrieved database goes into the tmp directory!
DB_NAME = "anime_database_tmp.sqlite3"
DB_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), os.path.join("tmp", DB_NAME))


class AniDatabaseRetriever:
    def __init__(self):
        self.anilist = Anilist()

        self.MAX_ANIME_ID = 300000
        self.BULK_WRITE_THRESHOLD = 1
        self.RETRIEVER_VERSION = 'V2.2-SQLite3'
        self.RATELIMIT_OFFSET = 0.75
        self.ANILISTPYTHON_VERSION = __version__

        self.records = 0
        self.db_conn = sqlite3.connect(DB_PATH)

    def create_database(self):
        cur = self.db_conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS Anime (
                id              INTEGER PRIMARY KEY,
                name_romaji     TEXT,
                name_english    TEXT,
                starting_time   TEXT,
                ending_time     TEXT,
                cover_image     TEXT,
                banner_image    TEXT,
                airing_format   TEXT,
                airing_status   TEXT,
                airing_episodes INTEGER,
                season          TEXT,
                desc_para       TEXT,
                average_score   INTEGER,
                genres          TEXT,
                next_airing_ep  TEXT,
                is_adult        TEXT,
                popularity      TEXT,
                origin          TEXT,
                duration        TEXT,
                updated_at      TEXT,
                source          TEXT,
                url             TEXT,

                record_updated_on DATETIME NOT NULL
            );
        """)

        cur.execute(f"""
            CREATE TABLE IF NOT EXISTS Metadata (
                database_updated_on         DATETIME NOT NULL DEFAULT current_timestamp,
                retriever_version           TEXT NOT NULL DEFAULT '{self.RETRIEVER_VERSION}',
                anilistpython_version       TEXT NOT NULL DEFAULT '{__init__.__version__}'
            )
        """)
        cur.execute("INSERT INTO Metadata DEFAULT VALUES;")
        self.db_conn.commit()

    def bulk_insert(self, records: list):
        # self.db_conn.execute("DROP TABLE Anime_Records")

        # curr_time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        # print(f"[{curr_time}] Writing {self.BULK_WRITE_THRESHOLD} records into DB...")
        try:
            self.db_conn.executemany("INSERT INTO Anime_Records VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", records)
        except sqlite3.ProgrammingError as ex:   # 1. incorrect number of fields supplied
            raise(ex)
        except sqlite3.IntegrityError as ex:     # 2. type mismatch / duplicate primary key
            raise(ex)
        except sqlite3.OperationalError as ex:   # 3. requested table doesn't exist
            print(f"Request table does not exist, creating table...")
            self.create_database()
            self.bulk_insert(records) # single recursive call for insert after table creation

        self.db_conn.commit()

    def initialize_values(self):
        self.create_database()

        curr_record_id = 0
        prev_record = self.db_conn.execute("SELECT * FROM Anime_Records ORDER BY id DESC LIMIT 1").fetchall()
        if len(prev_record) > 0: curr_record_id = prev_record[0][0] + 1
        return curr_record_id

    def retrieve_anime_data(self):
        curr_record_id = 0
        prev_record = self.db_conn.execute("SELECT * FROM Anime_Records ORDER BY id DESC LIMIT 1").fetchall()
        if len(prev_record) > 0: curr_record_id = prev_record[0][0] + 1

        anime_records = []
        while curr_record_id < self.MAX_ANIME_ID:

            # bulk writes to db for every x record retrieved
            if len(anime_records) == self.BULK_WRITE_THRESHOLD:
                self.bulk_insert(anime_records)
                anime_records = []

            try:
                anime_data = self.anilist.get_anime_with_id(curr_record_id)
                anime_tuple = (curr_record_id,)
                for label, content in anime_data.items():
                    if isinstance(content, list):
                        content = "|".join(content)
                    if label == "next_airing_ep" and content != None:
                        content = "|".join([str(time) for time in content.values()])
                    anime_tuple += (content,)
                anime_tuple += (datetime.now().strftime("%m-%d-%Y %H:%M:%S"),)
                anime_records.append(anime_tuple)

                anime_name = anime_data["name_romaji"]
                curr_time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
                print(f"[{curr_time}] <{len(anime_records)} records pending> | Retrieving anime ID: {curr_record_id}, Anime Name: {anime_name}")

            except Exception as ex:
                curr_time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
                print(f"[{curr_time}] <{len(anime_records)} records pending> | Retrieving anime ID: {curr_record_id}... Anime with such ID does not exist...")

            curr_record_id += 1
            time.sleep(self.RATELIMIT_OFFSET)

    def convert_time(self, seconds):
        m, s = divmod(seconds, 60)
        h, m = divmod(m, 60)
        
        return "%d hr, %02d min, %02d secs" % (h, m, s)


    def run_retriever(self):
        start = time.time()

        curr_time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        header = f"\n\n=============================== [{curr_time}] ==============================="
        print(header)
        print(f"""
        Retriever Version: {self.RETRIEVER_VERSION}
        Internal Support: AnilistPython V{self.ANILISTPYTHON_VERSION}
        Ratelimit Offset: {self.RATELIMIT_OFFSET} secs
        SQL Bulk Writes Threshold: {self.BULK_WRITE_THRESHOLD} records
        Estimated Time Consumption: {self.convert_time((self.MAX_ANIME_ID - self.initialize_values()) * (self.RATELIMIT_OFFSET + 0.14))} [{self.MAX_ANIME_ID - self.initialize_values()} records]
        """)
        l = ['='] * (len(header) - 2)
        print("".join(l) + "\n\n")
        
        u_i = input("Continue? [y/n]")
        if u_i.lower() != "y": exit(0)

        self.create_database()

        s = time.time()
        self.retrieve_anime_data()
        print(f"avg: {((time.time() - s) / 3000)}")

        print("All records have been successfully retrieved... Program Terminating...")
        print(f"Time Consumption: [{self.convert_time(time.time() - start)}]")


if __name__ == "__main__":
    db_ret = AniDatabaseRetriever()
    db_ret.run_retriever()
