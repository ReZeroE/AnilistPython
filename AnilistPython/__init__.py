import sys
import time
import requests

from .anime import Anime
from .character import Character
from .manga import Manga
from .deep_search import DeepSearch

from .databases.database_anime_retrieval import DatabaseSearcher
from .databases.search_engine import SearchEngine

from .anilistpython_info import AnilistPythonInfo

from .logs.setup_module import Setup
from .logs.log_data import LogData


class Anilist:
    """
        Initialize a new instance to the Anilist driver API.
        The instance is responsible for all search and retrieve operations. 
        In calls that require a user's auth token, you will need to provide it.
        :ivar dict access: Access required data used through out the program
        :ivar ALAuth auth: Handle Authorization endpoints
    """
    def __init__(self, cid = None, csecret = None, credentials = None, activated = True):
        """
        :param cid: Client ID
        :param csecret: Client Secret
        :param credentials: If provided, a JWT token for auth requests
        :param: activated: Bot Support - ensures that the program is activated. Default = True
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

        self.setup = Setup()
        self.log_data = LogData()


    def help(self):
        '''
        Prints a basic explanation on the functionalities of this module. Includes links where help could be found.
        '''
        api_help = AnilistPythonInfo()
        api_help.help()

    # ANIME =====================================================================================================================
    def get_anime_id(self, anime_name, manual_select=False) -> int:
        '''
        Retrieves the anime ID on Anilist.

        :param anime_name: The name of the anime
        :manual_select: prompts the user the top three results to select in the terminal
        :return: The anime's ID on Anilist. Returns -1 if an error is caught.
        :rtype: int
        '''      

        return self.anime.getAnimeID(anime_name, manual_select)

    def get_anime(self, anime_name, deepsearch=False, manual_select=False) -> dict:
        '''
        Retrieve the anime info in the form of a dictionary.

        :param anime_name: the name of the anime
        :param deepsearch: deepsearch control value. False by default.
        :manual_select: prompts the user the top three results to select in the terminal
        :return: parsed dict containing the anime's data
        :rtype: dict
        '''

        # deepsearch
        if deepsearch == True:
            ds = DeepSearch()
            return self.anime.getAnime(ds.deep_search_name_conversion(anime_name), manual_select)

        # normal search
        else:
            return self.anime.getAnime(anime_name, manual_select)

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
        
    def print_anime_info(self, anime_name):
        '''
        Displays all anime data.
        Auto formats the displayed version of the data.

        :param anime_name: The name of the anime
        '''

        self.anime.displayAnimeInfo(anime_name)

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
    def get_character_id(self, character_name, manual_select=False) -> int:
        '''
        Retrieves the character ID on Anilist.

        :param character_name: The character of the anime
        :manual_select: prompts the user the top three results to select in the terminal
        :return: The character's ID on Anilist. Returns -1 if an error is caught.
        :rtype: int
        '''
        return self.character.getCharacterID(character_name, manual_select)

    def get_character(self, character_name, manual_select=False) -> dict:
        '''
        Retrieve the character info in the form of a dictionary.

        :param anime_name: the name of the character
        :manual_select: prompts the user the top three results to select in the terminal
        :return: parsed dict containing the character's data
        :rtype: dict
        '''
        return self.character.getCharacter(character_name, manual_select)

    def get_character_with_id(self, character_id) -> dict:
        '''
        Retrieve character info in the form of a dictionary with the character's ID on Anilist.

        :param character_name: The name of the character
        :return: parsed dict containing the character's data
        :rtype: dict
        '''
        return self.character.getCharacterWithID(character_id)

    def print_character_info(self, character_name, manual_select=False):
        '''
        Displays all character data.
        Auto formats the displayed version of the data.

        :param character_name: The name of the character
        :manual_select: prompts the user the top three results to select in the terminal
        '''
        self.character.displayCharacterInfo(character_name, manual_select)

    # Manga =====================================================================================================================
    def get_manga_id(self, manga_name, manual_select=False) -> int:
        '''
        Displays all character data.
        Auto formats the displayed version of the data.

        :param character_name: The manga's name
        :manual_select: prompts the user the top three results to select in the terminal
        :return: the id of the manga
        :rtype: int
        '''
        return self.manga.getMangaID(manga_name, manual_select)

    def get_manga(self, manga_name, manual_select=False) -> dict:
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