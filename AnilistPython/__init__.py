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
__autoformat__  = False


import sys
import time
import requests

from anime import Anime
from character import Character
from manga import Manga
from utils.deepsearch.deep_search import DeepSearch
from databases.database_anime_retrieval import DatabaseSearcher
from databases.search_engine import SearchEngine

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

    def get_anime_from_database(self, anime_name) -> list:
        '''
        Retrieve the anime info in the form of a dictionary (from the local database).

        :param anime_name: the name of the anime
        :param deepsearch: deepsearch control value. False by default.
        :return: a list of dictionaries containing all the search results.
        :rtype: list
        '''
        se = SearchEngine()
        return se.search_anime_database(anime_name)

    def get_anime_with_id(self, anime_id) -> dict:
        '''
        Retrieve anime info in the form of a dictionary using the anime's ID.

        :param anime_id: The ID of the anime on Anilist
        :rtype: dict
        '''

        return self.anime.getAnimeWithID(anime_id)
        
    def print_anime_info(self, anime_name, count=3, title_colored=True):
        '''
        Displays all anime data.
        Auto formats the displayed version of the data.

        :param anime_name: The name of the anime
        '''

        self.anime.displayAnimeInfo(anime_name, count, title_colored)

    def search_anime(self, genre=None, year=None, score=None, id_only=False) -> list:
        '''
        Searches anime with genre, season, and/or year. Returns a list of anime within the given restrictions.
        Auto formats the displayed version of the data. (Accesses local database only)

        :param retrieve_count: Max number of anime records to be retrieved. Retrieve all (-1) by default.
        :param genre: The genre of the anime in str or list of str (i.e. 'Action' or ['Action', 'Romance'])
        :param year: The year of the anime in str or list of str (i.e. '2012' or ['2012', '2013'])
        :param score: The score of the anime in str as in range (i.e. '50' or '50-60' or range(50, 60))
        :param id_only: Only retrieve the ID of the anime. False by default.

        :return: a list of parsed dict containing the anime's data
        :rtype: list
        '''
        database_searcher = DatabaseSearcher()
        return database_searcher.anime_mix_search(genre=genre, year=year, score=score, id_only=id_only)

    # CHARACTER =================================================================================================================
    def get_character_id(self, character_name, count=1, manual_select=False) -> int:
        '''
        Retrieves the character ID on Anilist.

        :param character_name: The character of the anime
        :manual_select: prompts the user the top three results to select in the terminal
        :return: The character's ID on Anilist. Returns -1 if an error is caught.
        :rtype: int
        '''
        return self.character.getCharacterID(character_name, manual_select)

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

    def print_manga_info(self, manga_name, manual_select=False):
        '''
        Displays all manga data.
        Auto formats the displayed version of the data.

        :param manga_name: The name of the manga
        :manual_select: prompts the user the top three results to select in the terminal
        '''

        self.manga.displayMangaInfo(manga_name, manual_select)