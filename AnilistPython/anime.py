import time
import requests
from .retrieve_data import ExtractInfo
from .retrieve_id import ExtractID

class Anime:
    def __init__(self, access_info, activated=True):
        self.extractInfo = ExtractInfo(access_info, activated)
        self.extractID = ExtractID(access_info, activated)


    def getAnime(self, anime_name, manual_select=False) -> dict:
        '''
        Retrieve anime info in the form of a json object.
        Retrieve json object will be reformatted in a easily accessable json obj.

        :param anime_name: The name of the anime
        :return: parsed dict containing the anime's data
        :rtype: dict
        '''

        anime_id = self.getAnimeID(anime_name, manual_select)
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

        
    def getAnimeWithID(self, anime_id) -> dict:
        '''
        Retrieve anime info in the form of a json object.
        Retrieve json object will be reformatted in a easily accessable json obj.

        :param anime_name: The name of the anime
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


    def getAnimeID(self, anime_name, manual_select=False):
        '''
        Retrieves the anime ID on Anilist.

        :param anime_name: The name of the anime
        :return: The anime's ID on Anilist. Returns -1 if an error is caught.
        :rtype: int
        '''

        # if manual select is turned off ============================================================================
        if manual_select == False:
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

        # if manual select is turned on =============================================================================
        elif manual_select == True:
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

        else:
            # placeholder
            pass


    def displayAnimeInfo(self, anime_name, manual_select=False):
        '''
        Displays all anime data.
        Auto formats the displayed version of the data.

        :param anime_name: The name of the anime
        '''

        ani_dict = self.getAnime(anime_name, manual_select)
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