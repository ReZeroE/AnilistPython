# SPDX-License-Identifier: MIT
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


__version__     = "1.0.0"
__author__      = "Kevin L."
__name__        = "AnilistPython"
__license__     = "MIT License"

auto_format     = False


import sys
import time
import requests

# Supported Anilist Submodules
from anime      import Anime
from character  import Character
from manga      import Manga

# Database Submodules
from databases.db_update.update_db          import DatabaseUpdateTool
from databases.db_search.anime_db_handler   import AnimeDatabaseHandler
from databases.db_search.anime_db_handler   import AnimeGenres

# Utilities
from utils.deepsearch.deep_search import DeepSearch


# ================================
# ==========| ANILIST |===========
# ================================
class Anilist:
    """
    Initialize a new instance to the Anilist driver API.
    The instance is responsible for all search and retrieve operations. 
    In calls that require a user's auth token, you will need to provide it.
    :ivar dict access: Access required data used through out the program
    :ivar ALAuth auth: Handle Authorization endpoints
    """
    def __init__(self, cid=None, csecret=None, credentials=None, activated=True):
        """
        :param cid: Client ID
        :param csecret: Client Secret
        :param credentials: If provided, a JWT token for auth requests
        :param: activated: Bot Support - ensures that the program is activated. Default=True
        """
        self.access = {'header': {'Content-Type': 'application/json',
                                    'User-Agent': 'AnilistPython (github.com/ReZeroE/AnilistPython)',
                                    'Accept': 'application/json'},
                         'authurl': 'https://anilist.co/api',
                         'apiurl': 'https://graphql.anilist.co',
                         'cid': cid,
                         'csecret': csecret,
                         'token': credentials}

        self.anime = Anime(self.access, activated)
        self.character = Character(self.access, activated)
        self.manga = Manga(self.access, activated)
        self.version = __version__

    def help(self):
        '''
        Prints a basic explanation on the functionalities of this module. Includes links where help could be found.
        '''
        print("\nFor the full documentation, please visit <https://github.com/ReZeroE/AnilistPython>.", file=sys.stdout)
        sys.stdout.flush()

    # ANIME =====================================================================================================================
    def get_anime_id(self, anime_name, count=1, manual_select=False) -> list:
        '''
        Retrieves the anime ID on Anilist.

        :param anime_name: The name of the anime
        :manual_select: prompts the user the top three results to select in the terminal
        :return: The anime's ID on Anilist. Returns -1 if an error is caught.
        :rtype: int
        '''      
        if __autoformat__:
            id_list = self.anime.getAnimeID(anime_name, count, manual_select)
            if len(id_list) == 1: return id_list[0]
        else:
            return self.anime.getAnimeID(anime_name, count, manual_select)

    def get_anime(self, anime_name, count=3, deepsearch=False, manual_select=False) -> list:
        '''
        Retrieve the anime info in the form of a dictionary.

        :param anime_name: the name of the anime
        :param deepsearch: deepsearch control value. False by default.
        :manual_select: prompts the user the top three results to select in the terminal
        :return: A list of anime data dictionaries
        :rtype: list
        '''
        # ===============================
        # ======== | DeepSearch | =======
        # ===============================
        if deepsearch == True:
            ds = DeepSearch()
            if __autoformat__:
                ani_data = self.anime.getAnime(ds.deep_search_name_conversion(anime_name), count, manual_select)
                if len(ani_data) == 1: return ani_data[0]
            else:
                return self.anime.getAnime(ds.deep_search_name_conversion(anime_name), count, manual_select)

        # ===============================
        # ====== | Normal Search | ======
        # ===============================
        else:
            if __autoformat__:
                ani_data = self.anime.getAnime(anime_name, count, manual_select)
                if len(ani_data) == 1: return ani_data[0]
            else:
                return self.anime.getAnime(anime_name, count, manual_select)

    def get_anime_with_id(self, anime_id) -> dict:
        '''
        Retrieve anime info in the form of a dictionary using the anime's ID.

        :param anime_id: The ID of the anime on Anilist
        :rtype: dict
        '''

        return self.anime.getAnimeWithID(anime_id)
        
    def print_anime_info(self, anime_name, count=3, manual_select=False, title_colored=True):
        '''
        Displays all anime data.
        Auto formats the displayed version of the data.

        :param anime_name: The name of the anime
        '''

        self.anime.displayAnimeInfo(anime_name, count, manual_select, title_colored)


    # CHARACTER =================================================================================================================
    def get_character_id(self, character_name, count=1, manual_select=False) -> int:
        '''
        Retrieves the character ID on Anilist.

        :param character_name: The character of the anime
        :manual_select: prompts the user the top three results to select in the terminal
        :return: The character's ID on Anilist. Returns -1 if an error is caught.
        :rtype: int
        '''
        return self.character.getCharacterIDs(character_name, manual_select)

    def get_character(self, character_name, count=3, manual_select=False) -> dict:
        '''
        Retrieve the character info in the form of a dictionary.

        :param anime_name: the name of the character
        :manual_select: prompts the user the top three results to select in the terminal
        :return: parsed dict containing the character's data
        :rtype: dict
        '''
        return self.character.getCharacter(character_name, count, manual_select)

    def get_character_with_id(self, character_id) -> dict:
        '''
        Retrieve character info in the form of a dictionary with the character's ID on Anilist.

        :param character_name: The name of the character
        :return: parsed dict containing the character's data
        :rtype: dict
        '''
        return self.character.getCharacterWithID(character_id)

    def print_character_info(self, character_name, count=3, manual_select=False, name_colored=True):
        '''
        Displays all character data.
        Auto formats the displayed version of the data.

        :param character_name: The name of the character
        :manual_select: prompts the user the top three results to select in the terminal
        '''
        self.character.displayCharacterInfo(character_name, count, manual_select, name_colored)


    # Manga =====================================================================================================================
    def get_manga_id(self, manga_name, count=3, manual_select=False) -> int:
        '''
        Displays all character data.
        Auto formats the displayed version of the data.

        :param character_name: The manga's name
        :manual_select: prompts the user the top three results to select in the terminal
        :return: the id of the manga
        :rtype: int
        '''
        return self.manga.getMangaIDs(manga_name, count, manual_select)

    def get_manga(self, manga_name, count=3, manual_select=False) -> dict:
        '''
        Retrieve manga info in the form of a dictionary.

        :param manga_name: The name of the manga
        :return: parsed dict containing the manga's data
        :manual_select: prompts the user the top three results to select in the terminal
        :rtype: dict
        '''

        return self.manga.getManga(manga_name, manual_select)

    def get_manga_with_id(self, manga_id) -> dict:
        '''
        Retrieve manga info in the form of a dictionary with the manga's ID on Anilist.

        :param manga_id: The id of the manga
        :return: parsed dict containing the manga's data
        :rtype: dict
        '''
        return self.manga.getMangaWithID(manga_id)

    def print_manga_info(self, manga_name, count=1, manual_select=False, title_colored=True):
        '''
        Displays all manga data.
        Auto formats the displayed version of the data.

        :param manga_name: The name of the manga
        :manual_select: prompts the user the top three results to select in the terminal
        '''

        self.manga.displayMangaInfo(manga_name, count, manual_select, title_colored)


# =======================================
# ==========| ANIME DATABASE |===========
# =======================================
class AnimeDatabase:
    """
    Anime database handler class. 
    Provides a variety of anime database search and utility functions.
    """
    def __init__(self):
        self.curr_db_ver = 0
        self.database_handler = AnimeDatabaseHandler()

    def update_db(self, verbose=True):
        """
        Update the local database to the newest version. Requires an internet connection.

        :param verbose: Verbose progress. Default to True.
        """
        if verbose == True:
            print(f"[AnilistPython {__version__}] Updating local database...", end=' ')
            sys.stdout.flush()

        db_update_tool = DatabaseUpdateTool()
        db_update_tool.update_db()
        time.sleep(1)

        if verbose == True:
            print("DONE")
            sys.stdout.flush()

    def search_by_id(self, anime_id) -> list:
        """
        Search local Anime database by the anime's ID.

        :param anime_id: The anime's ID to search

        :return: The anime's data
        :rtype: dict
        """
        return self.database_handler.search_anime_db_by_id(anime_id)

    def search_by_name(self, anime_name, id_only=False, case_sensitive=True, match_threshold=None) -> list:
        """
        Search anime by name from the local database.

        :param anime_name: The name of the anime to search.
        :param id_only: Return only the IDs of the anime found. Default to False.
        :param case_sensitive: Search case sensitivity. Default to True.
        :param match_threshold: The match threshold ratio for the search. Ranges between 0-100. Default to 80.

        :return: A list of anime with matching names.
        :rtype: list
        """
        return self.database_handler.search_anime_db_by_name(anime_name, id_only, case_sensitive, match_threshold)

    def search_by_release_year(self, release_year, id_only=False) -> list:
        """
        Search anime by release year from the local database.

        :param release_year: The release date of the anime. This value can be a range. (i.e. 2018 or range(2017, 2022))
        :param id_only: Return only the IDs of the anime found. Default to False.

        :return: A list of anime with the given release year.
        :rtype: list
        """
        return self.database_handler.search_anime_db_by_release_year(release_year, id_only)

    def search_by_season(self, release_season, id_only=False) -> list:
        """
        Search anime by release season from the local database.

        :param release_season: The release season of the anime. ('Spring', 'Summer', 'Fall', or 'Winter')
        :param id_only: Return only the IDs of the anime found. Default to False.

        :return: A list of anime released in the given season.
        :rtype: list
        """
        return self.database_handler.search_anime_db_by_release_season(release_season, id_only)

    def search_by_genre(self, genre, id_only=False) -> list:
        """
        Search anime by genre(s) from the local database.

        :param genre: The genre(s) of the anime. Can be either a list of a str. (i.e. 'action' or ['mahou shoujo', 'drama'])
        :param id_only: Return only the IDs of the anime found. Default to False.
        
        :return: A list of anime with the target genre(s).
        :rtype: list
        """
        return self.database_handler.search_anime_db_by_genre(genre, id_only)

    def get_genres_list(self):
        """
        Returns a list of all the searchable genres.
        """
        return self.database_handler.get_genre_list()

    

    