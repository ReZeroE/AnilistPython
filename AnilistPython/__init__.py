import time
import requests
from .extractInfo import ExtractInfo
from .extractID import ExtractID

class Anilist:
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


    # DRIVER SUPPORTED FUNCTIONS ==============================================================
    def getAnimeID(self, anime_name):
        '''
        Retrieves the anime ID on Anilist.

        :param anime_name: The name of the anime
        :return: The anime's ID on Anilist. Returns -1 if an error is caught.
        :rtype: int
        '''

        data = self.extractID.anime(anime_name)
        max_result = 0
        counter = 0 # number of displayed results from search
        for i in range(len(data['data']['Page']['media'])):
            curr_anime = data['data']['Page']['media'][i]['title']['romaji']
            print(f"{counter + 1}. {curr_anime}")
            max_result = i + 1
            counter += 1
        
        if counter > 1: # only one result found if counter == 1
            try:
                user_input = int(input("Please select the anime that you are searching for in number: "))
            except TypeError:
                print(f"Your input is incorrect! Please try again!")
                return -1

            if user_input > max_result or user_input <= 0:
                print("Your input does not correspound to any of the anime displayed!")
                return -1
        elif counter == 0:
            print(f'No search result has been found for the anime "{anime_name}"!')
            return -1
        else:
            user_input = 1

        return data['data']['Page']['media'][user_input - 1]['id']


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

    def printAnimeInfo(self, anime_name):
        '''
        Displays all anime data.
        Auto formats the displayed version of the data.

        :param anime_name: The name of the anime
        '''

        ani_dict = self.getAnimeInfo(anime_name)
        if ani_dict == None:
            print('Name Error')
        else:
            arr = ["Name(romaji)", "Name(Eng)", "Started Airing On", "Ended On", "Cover Image", "Banner Image",
            "Airing Format", "Airing Status", "Total Ep Count", "Season", "Description", "Ave. Score", "Genres",
            "Next Ep Airing Date"]
            counter = 0

            print("====================================================================")
            print("============================ ANIME INFO ============================")
            for key, value in ani_dict.items():
                print(f"{arr[counter]}: {value}")
                counter += 1

    # CHARACTER =================================================================================================
    def getCharacterID(self, character_name):
        '''
        Retrieves the character ID on Anilist.

        :param character_name: The character of the anime
        :return: The character's ID on Anilist. Returns -1 if an error is caught.
        :rtype: int
        '''

        max_result = 0
        counter = 0 # number of displayed results from search
        data = self.extractID.character(character_name)
        for i in range(len(data['data']['Page']['characters'])):
            first_name = data['data']['Page']['characters'][i]['name']['first']
            last_name = data['data']['Page']['characters'][i]['name']['last']
            max_result = i + 1

            if last_name == None:
                print(f"{counter + 1}. {first_name}")
            elif first_name == None:
                print(f"{counter + 1}. {last_name}")
            else:
                print(f'{counter + 1}. {last_name}, {first_name}')
            counter += 1

        if counter > 1: # only one result found if counter == 1
            try:
                user_input = int(input("Please select the character that you are searching for in number: "))
            except TypeError:
                print(f"Your input is incorrect! Please try again!")
                return -1
            
            if user_input > max_result or user_input <= 0:
                print("Your input does not correspound to any of the characters!")
                return -1
        elif counter == 0:
            print(f'No search result has been found for the character "{character_name}"!')
            return -1
        else:
            user_input = 1

        return data['data']['Page']['characters'][user_input - 1]['id']

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

    def printCharacterInfo(self, character_name):
        '''
        Displays all character data.
        Auto formats the displayed version of the data.

        :param character_name: The character of the anime
        '''

        char_dict = self.getCharacterInfo(character_name)
        if char_dict == None:
            print("Character Search Error")
        else:
            arr = ["First Name", "Last Name", "Japanese Name", "Description", "Image"]
            counter = 0

            print("========================================================================")
            print("============================ CHARACTER INFO ============================")
            for key, value in char_dict.items():
                print(f"{arr[counter]}: {value}")
                counter += 1
