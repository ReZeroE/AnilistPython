import time
import requests
from retrieve_data import ExtractInfo
from retrieve_id import ExtractID


class botSupportClass:
    """
        Initialize a new instance to the Anilist driver API.
        The instance is responsible for all read operations. 
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

        self.extractInfo = ExtractInfo(self.access, activated)
        self.extractID = ExtractID(self.access, activated)
        self.activated = activated


    # ANIME ===============================================================================================================
    def getAnimeID(self, anime_name) -> int:
        '''
        Retrieves the anime ID on Anilist. (First match)

        :param anime_name: The name of the anime
        :return: The anime's ID on Anilist. Returns the first match.
        :rtype: int
        '''
        anime_list = []
        data = self.extractID.anime(anime_name)
        for i in range(len(data['data']['Page']['media'])):
            curr_anime = data['data']['Page']['media'][i]['title']['romaji']
            anime_list.append(curr_anime)

        # returns the first anime found
        try:
            anime_ID = data['data']['Page']['media'][0]['id']
        except IndexError:
            raise IndexError('Anime Not Found')

        return anime_ID


    def getAnimeInfo(self, anime_name) -> dict:
        '''
        Retrieve anime info in the form of a json object.
        Retrieve json object will be reformatted in a easily accessable json obj.

        :param anime_name: The name of the anime
        :return: parsed dict containing the anime's data
        :rtype: dict
        '''

        anime_id = self.getAnimeID(anime_name)
        if anime_id == -1:
            return None

        data = self.extractInfo.anime(anime_id)
        media_lvl = data['data']['Media']

        name_romaji = media_lvl['title']['romaji']
        name_english = media_lvl['title']['english']

        start_year = media_lvl['startDate']['year']
        start_month = media_lvl['startDate']['month']
        start_day = media_lvl['startDate']['day']

        end_year = media_lvl['endDate']['year']
        end_month = media_lvl['endDate']['month']
        end_day = media_lvl['endDate']['day']

        starting_time = f'{start_month}/{start_day}/{start_year}'
        ending_time = f'{end_month}/{end_day}/{end_year}'

        cover_image = media_lvl['coverImage']['large']
        banner_image = media_lvl['bannerImage']

        airing_format = media_lvl['format']
        airing_status = media_lvl['status']
        airing_episodes = media_lvl['episodes']
        season = media_lvl['season']

        desc = media_lvl['description']

        average_score = media_lvl['averageScore']
        genres = media_lvl['genres']

        next_airing_ep = media_lvl['nextAiringEpisode']

        anime_dict = {"name_romaji": name_romaji,
                    "name_english": name_english,
                    "starting_time": starting_time,
                    "ending_time": ending_time,
                    "cover_image": cover_image,
                    "banner_image": banner_image,
                    "airing_format": airing_format,
                    "airing_status": airing_status,
                    "airing_episodes": airing_episodes,
                    "season": season,
                    "desc": desc,
                    "average_score": average_score,
                    "genres": genres,
                    "next_airing_ep": next_airing_ep,}

        return anime_dict


    def getAnimeInfoWithID(self, anime_id):
        '''
        Retrieve anime info in the form of a json object given the ID.
        Retrieve json object will be reformatted in a easily accessable json obj.

        :param anime_id: The ID of the anime
        :return: parsed dict containing the anime's data
        :rtype: dict
        '''

        data = self.extractInfo.anime(anime_id)
        media_lvl = data['data']['Media']

        name_romaji = media_lvl['title']['romaji']
        name_english = media_lvl['title']['english']

        start_year = media_lvl['startDate']['year']
        start_month = media_lvl['startDate']['month']
        start_day = media_lvl['startDate']['day']

        end_year = media_lvl['endDate']['year']
        end_month = media_lvl['endDate']['month']
        end_day = media_lvl['endDate']['day']

        starting_time = f'{start_month}/{start_day}/{start_year}'
        ending_time = f'{end_month}/{end_day}/{end_year}'

        cover_image = media_lvl['coverImage']['large']
        banner_image = media_lvl['bannerImage']

        airing_format = media_lvl['format']
        airing_status = media_lvl['status']
        airing_episodes = media_lvl['episodes']
        season = media_lvl['season']

        desc = media_lvl['description']

        average_score = media_lvl['averageScore']
        genres = media_lvl['genres']

        next_airing_ep = media_lvl['nextAiringEpisode']

        anime_dict = {"name_romaji": name_romaji,
                    "name_english": name_english,
                    "starting_time": starting_time,
                    "ending_time": ending_time,
                    "cover_image": cover_image,
                    "banner_image": banner_image,
                    "airing_format": airing_format,
                    "airing_status": airing_status,
                    "airing_episodes": airing_episodes,
                    "season": season,
                    "desc": desc,
                    "average_score": average_score,
                    "genres": genres,
                    "next_airing_ep": next_airing_ep,}

        return anime_dict
    
    # CHARACTER ===========================================================================================================
    def getCharacterID(self, character_name):
        '''
        Retrieves the character ID on Anilist.

        :param character_name: The character of the anime
        :return: The character's ID on Anilist. Returns -1 if an error is caught.
        :rtype: int
        '''

        character_list = []
        data = self.extractID.character(character_name)
        for i in range(len(data['data']['Page']['characters'])):
            first_name = data['data']['Page']['characters'][i]['name']['first']
            last_name = data['data']['Page']['characters'][i]['name']['last']
            character_list.append([first_name, last_name])

        try:
            character_ID = data['data']['Page']['characters'][0]['id']
        except IndexError:
            raise IndexError('Character Not Found')

        return character_ID


    def getCharacterInfo(self, character_name):
        '''
        Retrieve character info in the form of a json object.
        Retrieve json object will be reformatted in a easily accessable json obj.

        :param character_name: The name of the character
        :return: parsed dict containing the character's data
        :rtype: dict
        '''

        character_id = self.getCharacterID(character_name)
        if character_id == -1:
            return None

        data = self.extractInfo.character(character_id)
        character_lvl = data['data']['Character']

        first_name = character_lvl['name']['first']
        last_name = character_lvl['name']['last']
        native_name = character_lvl['name']['native']

        desc = character_lvl['description']
        image = character_lvl['image']['large']

        character_dict = {"first_name": first_name,
                        "last_name": last_name,
                        "native_name": native_name,
                        "desc": desc,
                        "image": image,}

        return character_dict


    def getCharacterInfoWithID(self, character_id):
        '''
        Retrieve character info in the form of a json object given the character's ID.
        Retrieve json object will be reformatted in a easily accessable json obj.

        :param character_id: The ID of the character
        :return: parsed dict containing the character's data
        :rtype: dict
        '''

        data = self.extractInfo.character(character_id)
        character_lvl = data['data']['Character']

        first_name = character_lvl['name']['first']
        last_name = character_lvl['name']['last']
        native_name = character_lvl['name']['native']

        desc = character_lvl['description']
        image = character_lvl['image']['large']

        character_dict = {"first_name": first_name,
                        "last_name": last_name,
                        "native_name": native_name,
                        "desc": desc,
                        "image": image,}

        return character_dict
    
