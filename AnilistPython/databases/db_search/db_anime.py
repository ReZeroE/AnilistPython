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

import os
import sys
import rapidfuzz
import sqlite3

class AnimeDatabase:

    def __init__(self):
        self.match_threshold = 0.9
        self.db = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../anime_database.sqlite3")

    def get_conn(self):
        return sqlite3.connect(self.db)

    def search_anime_db_by_name(self, anime_name):
        cur = self.get_conn().cursor()

        sql = f"SELECT id, name_romaji, name_english FROM Anime_Records"
        cur.execute(sql)
        db_retrieved_anime_names = cur.fetchall()

        # Generate a dictionary (key=anime_id) based on the anime data retrieved from the DB
        db_dict = dict()
        for id, name_romaji, name_english in db_retrieved_anime_names:
            if name_english == None and name_english == None:
                continue
            elif name_english == None and name_romaji != None:
                db_dict.setdefault(id, []).append([name_romaji])
            elif name_english != None and name_romaji == None:
                db_dict.setdefault(id, []).append([name_english])
            else:
                db_dict.setdefault(id, []).append(list(set([name_romaji, name_english])))


        results = []
        for k, v in db_dict:
            for anime_name_db in v:
                acc = rapidfuzz.fuzz.ratio(anime_name, anime_name_db)
                if acc > self.match_threshold:
                    pass




if __name__ == "__main__":
    # print(rapidfuzz.fuzz.ratio("hwllo world", "hello world"))
    ad = AnimeDatabase()

    ad.search_anime_db_by_name('')
    