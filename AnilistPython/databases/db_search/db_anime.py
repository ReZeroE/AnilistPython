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
import re
import sys
import rapidfuzz
import sqlite3
from copy import deepcopy

class AnimeDatabase:
    """
    Anime Database Handler Class. Provides DB search functions.

    Optimization Update:
     - Loaded tables are now buffered in memery to reduce the I/O operation time.
     - String fuzz is replaced with rapidfuzz, speeding up name matching operations drastically (around 90%). 
    """

    def __init__(self):
        """
        Initialize AnimeDatabase class.
        Sets match threshold and DB path.
        """
        self.match_threshold = 80
        self.db = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../anime_database.sqlite3")

        self.database_content = dict()
        self.database_columns = []


    def get_conn(self):
        '''
        Establish connection to the target SQLite DB.
        :return: SQLite Connection
        '''
        return sqlite3.connect(self.db)


    def search_anime_db_by_id(self, anime_id) -> dict:
        """
        Search local Anime database by the anime's ID.

        :param anime_id: The anime's ID to search
        :return: The anime's data
        :rtype: dict
        """
        # ================================
        # ======| PARSE USER INPUT |======
        # ================================
        try:
            anime_id = int(anime_id)
        except:
            raise Exception(f"Your anime_id [{anime_id}] must be an Integer or a String representing an Integer. (Ex: 100049 or '100049')")

        # ==============================================
        # ======| READ DB INTO BUFFER FOR SEARCH |======
        # ==============================================
        cur = self.get_conn().cursor()

        if len(self.database_content) == 0:
            sql = f"SELECT * FROM Anime_Records"
            anime_db_data = cur.execute(sql)

            database_buffer = dict()
            db_columns = [c[0] for c in anime_db_data.description]

            anime_db_data = anime_db_data.fetchall()

            # Optimization (Buffer loaded data from DB to prevent multiple DB reads)
            self.database_content = deepcopy(anime_db_data)
            self.database_columns = deepcopy(db_columns)
        else:
            anime_db_data   = self.database_content
            db_columns      = self.database_columns


        # ============================================
        # ======| GENERATE RETURN DATA FROM DB |======
        # ============================================
        # Formates data into key value pairs for return
        for anime_data in anime_db_data:
            if anime_data[0] == anime_id:
                return dict(zip(db_columns, anime_data))

        return None


    def search_anime_db_by_name(self, anime_name, id_only=False, case_sensitive=True, match_threshold=None) -> list:
        """
        Search anime by name from the local database!

        :param anime_name: The name of the anime to search.
        :param id_only: Only the IDs of the anime found. Default to False.
        :param case_sensitive: Search case sensitivity. Default to True.
        :param match_threshold: The match threshold ratio for the search. Ranges between 0-100. Default to 80.
        :return: A list of anime with matching names.
        :rtype: list
        """
        # ================================
        # ======| PARSE USER INPUT |======
        # ================================
        try:
            anime_name = anime_name.strip()
        except:
            raise Exception(f"Your anime_name [{anime_name}] must be of type String.")


        # =====================================================
        # ======| SET USER DEFINED FUZZ MATCH THRESHOLD |======
        # =====================================================
        if isinstance(match_threshold, int) or isinstance(match_threshold, float):
            if match_threshold > 100 or match_threshold < 0:
                raise Exception(f"Your match_threshold value [{match_threshold}] is not within a valid range. It should range between 0-100")
            self.match_threshold = match_threshold


        # ==============================================
        # ======| READ DB INTO BUFFER FOR SEARCH |======
        # ==============================================
        cur = self.get_conn().cursor()

        if len(self.database_content) == 0:
            sql = f"SELECT * FROM Anime_Records"
            anime_db_data = cur.execute(sql)
            db_columns = [c[0] for c in anime_db_data.description]

            anime_db_data = anime_db_data.fetchall()

            # Optimization (Buffer loaded data from DB to prevent multiple DB reads)
            self.database_content = deepcopy(anime_db_data.fetchall())
            self.database_columns = deepcopy(db_columns)
        else:
            anime_db_data   = self.database_content
            db_columns      = self.database_columns

        # Generate a dictionary based on the anime data retrieved from the DB
        database_buffer     = dict()    # Dict with all data, buffers the entire Anime table
        anime_db_names_dict = dict()    # Dict with only ID and anime name
        for anime_data in anime_db_data:

            # ============================================
            # ======| CREATE DICT WITH ANIME NAMES |======
            # ============================================
            id              = anime_data[0]
            name_romaji     = anime_data[1]
            name_english    = anime_data[2]
            
            if name_english == None and name_english == None:
                continue
            elif name_english == None and name_romaji != None:
                anime_db_names_dict.setdefault(id, []).append(name_romaji)
            elif name_english != None and name_romaji == None:
                anime_db_names_dict.setdefault(id, []).append(name_english)
            else:
                for name in set([name_romaji, name_english]):
                    anime_db_names_dict.setdefault(id, []).append(name)

            # ================================
            # ======| CREATE DB BUFFER |======
            # ================================
            database_buffer[id] = dict(zip(db_columns, anime_data))


        # ===========================================
        # ======| RAPIDFUZZ MATCH ANIME NAMES |======
        # ===========================================
        results = []
        for anime_id, curr_anime_names in anime_db_names_dict.items():
            for anime_name_db in curr_anime_names:

                # Rapidfuzz anime name with partial ratio
                if case_sensitive == True:
                    acc = rapidfuzz.fuzz.partial_ratio(anime_name, anime_name_db)
                else:
                    acc = rapidfuzz.fuzz.partial_ratio(anime_name.lower(), anime_name_db.lower())

                # Anime with name found
                if acc > self.match_threshold:
                    if id_only == True:
                        results.append(anime_id)
                    else:
                        results.append(database_buffer[anime_id])
        return results


    def search_anime_db_by_release_year(self, release_year, id_only=False) -> list:
        """
        Search anime by release year from the local database!

        :param release_year: The release date of the anime. This value can be a range. (i.e. 2018 or range(2017, 2022))
        :param id_only: Only the IDs of the anime found. Default to False.
        :return: A list of anime with the given release year.
        :rtype: list
        """
        # ================================
        # ======| PARSE USER INPUT |======
        # ================================
        if isinstance(release_year, int) or isinstance(release_year, str):
            try:
                release_year = int(release_year)
            except:
                raise Exception(f"Your input year [{release_year}] is incorrect. It must be of type Integer or a String representing an integer. (Ex: 2021 or '2021')")
        elif isinstance(release_year, range):
            pass


        # ==============================================
        # ======| READ DB INTO BUFFER FOR SEARCH |======
        # ==============================================
        cur = self.get_conn().cursor()

        if len(self.database_content) == 0:
            sql = f"SELECT * FROM Anime_Records"
            anime_db_data = cur.execute(sql)
            db_columns = [c[0] for c in anime_db_data.description]

            anime_db_data = anime_db_data.fetchall()

            # Optimization (Buffer loaded data from DB to prevent multiple DB reads)
            self.database_content = deepcopy(anime_db_data)
            self.database_columns = deepcopy(db_columns)
        else:
            anime_db_data   = self.database_content
            db_columns      = self.database_columns



        # ============================================
        # ======| GENERATE RETURN DATA FROM DB |======
        # ============================================
        database_buffer = dict()

        # Formates data into key value pairs for return
        for anime_data in anime_db_data:
            id = anime_data[0]
            database_buffer[id] = dict(zip(db_columns, anime_data))


        # ============================================
        # ======| QUERY DB TARGET RELEASE YEAR |======
        # ============================================
        results = []
        for anime_data in anime_db_data:
            try:
                id              = anime_data[0]
                release_year_db = anime_data[4]
                release_year_db = int(release_year_db.split('/')[-1])
            except:
                continue

            # YEAR RANGE SEARCH
            if isinstance(release_year, range):
                release_year_range = release_year
                if release_year_db in release_year_range:
                    if id_only == True:     # Return anime IDs Only
                        results.append(id)
                    else:                   # Return anime data
                        results.append(database_buffer[id])

            # YEAR MATCH SEARCH
            elif isinstance(release_year, int):
                if release_year_db == release_year:
                    if id_only == True:     # Return anime IDs Only
                        results.append(id)
                    else:                   # Return anime data
                        results.append(database_buffer[id])
        return results


    def search_anime_db_by_release_season(self, release_season, id_only=False) -> list:
        """
        Search anime by release season from the local database!

        :param release_season: The release season of the anime. ('Spring', 'Summer', 'Fall', or 'Winter')
        :param id_only: Only the IDs of the anime found. Default to False.
        :return: A list of anime released in the given season.
        :rtype: list
        """
        # ================================
        # ======| PARSE USER INPUT |======
        # ================================
        try:
            release_season = release_season.strip().lower()
            if release_season not in ["spring", "summer", "fall", "winter"]:
                raise Exception(f"Your input season [{release_season}] is incorrect. It must be one of 'Spring', 'Summer', 'Fall', or 'Winter'.")
        except:
            raise Exception(f"Your input season [{release_season}] is incorrect. It must be one of 'Spring', 'Summer', 'Fall', or 'Winter'.")


        # ==============================================
        # ======| READ DB INTO BUFFER FOR SEARCH |======
        # ==============================================
        cur = self.get_conn().cursor()

        if len(self.database_content) == 0:
            sql = f"SELECT * FROM Anime_Records"
            anime_db_data = cur.execute(sql)
            db_columns = [c[0] for c in anime_db_data.description]

            anime_db_data = anime_db_data.fetchall()

            # Optimization (Buffer loaded data from DB to prevent multiple DB reads)
            self.database_content = deepcopy(anime_db_data)
            self.database_columns = deepcopy(db_columns)
        else:
            anime_db_data   = self.database_content
            db_columns      = self.database_columns


        # ============================================
        # ======| GENERATE RETURN DATA FROM DB |======
        # ============================================
        database_buffer = dict()

        # Formates data into key value pairs for return
        for anime_data in anime_db_data:
            id = anime_data[0]
            database_buffer[id] = dict(zip(db_columns, anime_data))


        # ============================================
        # ======| QUERY DB TARGET RELEASE YEAR |======
        # ============================================
        results = []
        for anime_data in anime_db_data:
            try:
                id          = anime_data[0]
                season_db   = anime_data[10]
                season_db   = season_db.lower()
            except:
                continue
            
            # Search for matching season
            if release_season == season_db:
                if id_only == True:     # Return anime IDs Only
                    results.append(id)
                else:                   # Return anime data
                    results.append(database_buffer[id])

        return results



if __name__ == "__main__":
    ad = AnimeDatabase()

    c = ad.search_anime_db_by_id(100049)
    c = ad.search_anime_db_by_name("code geass", id_only=True)
    c = ad.search_anime_db_by_release_year("2019", id_only=True)
    c = ad.search_anime_db_by_release_season("spring", id_only=True)

    