import time
import requests
from .retrieve_data import ExtractInfo
from .retrieve_id import ExtractID

class Manga:
    def __init__(self, access_info, activated=True):
        self.extractInfo = ExtractInfo(access_info, activated)
        self.extractID = ExtractID(access_info, activated)


    def getManga(self, manga_name, manual_select=False):
        '''
        Retrieve character info in the form of a json object.
        Retrieve json object will be reformatted in a easily accessable json obj.

        :param character_name: The name of the character
        :return: parsed dict containing the character's data
        :rtype: dict
        '''
        manga_dict = {}

        manga_id = self.getMangaID(manga_name, manual_select)
        if manga_id == -1:
            return None

        data = self.extractInfo.manga(manga_id)
        media_lvl = data['data']['Media']
        
        manga_dict['name_romaji'] = media_lvl['title']['romaji']
        manga_dict['name_english'] = media_lvl['title']['english']

        start_year = media_lvl['startDate']['year']
        start_month = media_lvl['startDate']['month']
        start_day = media_lvl['startDate']['day']

        end_year = media_lvl['endDate']['year']
        end_month = media_lvl['endDate']['month']
        end_day = media_lvl['endDate']['day']

        manga_dict['starting_time'] = f'{start_month}/{start_day}/{start_year}'
        manga_dict['ending_time'] = f'{end_month}/{end_day}/{end_year}'

        manga_dict['cover_image'] = media_lvl['coverImage']['large']
        manga_dict['banner_image'] = media_lvl['bannerImage']

        manga_dict['release_format'] = media_lvl['format']
        manga_dict['release_status'] = media_lvl['status']

        manga_dict['chapters'] = media_lvl['chapters']
        manga_dict['volumes'] = media_lvl['volumes']

        manga_dict['desc'] = media_lvl['description']

        manga_dict['average_score'] = media_lvl['averageScore']
        manga_dict['mean_score'] = media_lvl['meanScore']

        manga_dict['genres'] = media_lvl['genres']
        manga_dict['synonyms'] = media_lvl['synonyms']

        return manga_dict


    def getMangaWithID(self, manga_id) -> dict:
        '''
        Retrieve character info in the form of a json object.
        Retrieve json object will be reformatted in a easily accessable json obj.

        :param character_name: The name of the character
        :return: parsed dict containing the character's data
        :rtype: dict
        '''
        manga_dict = {}

        data = self.extractInfo.manga(manga_id)
        media_lvl = data['data']['Media']
        
        manga_dict['name_romaji'] = media_lvl['title']['romaji']
        manga_dict['name_english'] = media_lvl['title']['english']

        start_year = media_lvl['startDate']['year']
        start_month = media_lvl['startDate']['month']
        start_day = media_lvl['startDate']['day']

        end_year = media_lvl['endDate']['year']
        end_month = media_lvl['endDate']['month']
        end_day = media_lvl['endDate']['day']

        manga_dict['starting_time'] = f'{start_month}/{start_day}/{start_year}'
        manga_dict['ending_time'] = f'{end_month}/{end_day}/{end_year}'

        manga_dict['cover_image'] = media_lvl['coverImage']['large']
        manga_dict['banner_image'] = media_lvl['bannerImage']

        manga_dict['release_format'] = media_lvl['format']
        manga_dict['release_status'] = media_lvl['status']

        manga_dict['chapters'] = media_lvl['chapters']
        manga_dict['volumes'] = media_lvl['volumes']

        manga_dict['desc'] = media_lvl['description']

        manga_dict['average_score'] = media_lvl['averageScore']
        manga_dict['mean_score'] = media_lvl['meanScore']

        manga_dict['genres'] = media_lvl['genres']
        manga_dict['synonyms'] = media_lvl['synonyms']

        return manga_dict


    def getMangaID(self, manga_name, manual_select=False):
        '''
        Retrieves the character ID on Anilist.

        :param character_name: The character of the Manga
        :return: The character's ID on Anilist. Returns -1 if an error is caught.
        :rtype: int
        '''

        if manual_select == False:
            manga_list = []
            data = self.extractID.manga(manga_name)
            for i in range(len(data['data']['Page']['media'])):
                curr_manga = data['data']['Page']['media'][i]['title']['romaji']
                manga_list.append(curr_manga)

            print(manga_list)

            # returns the first manga found
            try:
                manga_ID = data['data']['Page']['media'][0]['id']
            except IndexError:
                raise IndexError('Manga Not Found')

            return manga_ID


        elif manual_select == True:
            max_result = 0
            counter = 0 # number of displayed results from search
            data = self.extractID.manga(manga_name)
            for i in range(len(data['data']['Page']['media'])):
                curr_manga = data['data']['Page']['media'][i]['title']['romaji']
                print(f"{counter + 1}. {curr_manga}")
                max_result = i + 1
                counter += 1
            
            if counter > 1: # only one result found if counter == 1
                try:
                    user_input = int(input("Please select the manga that you are searching for in number: "))
                except TypeError or ValueError:
                    print(f"Your input is incorrect! Please try again!")
                    return -1

                if user_input > max_result or user_input <= 0:
                    print("Your input does not correspound to any of the manga displayed!")
                    return -1
            elif counter == 0:
                print(f'No search result has been found for the manga "{manga_name}"!')
                return -1
            else:
                user_input = 1

            return data['data']['Page']['media'][user_input - 1]['id']
        
        else:
            # placeholder
            pass


    def displayMangaInfo(self, manga_name, manual_select=False):
        '''
        Displays all character data.
        Auto formats the displayed version of the data.

        :param character_name: The character of the Manga
        '''

        manga_dict = self.getManga(manga_name, manual_select)
        if manga_dict == None:
            print("Manga Search Error - Manga Not Found")
        else:
            arr = ['name_romaji', 'name_english', 'starting_time', 'ending_time', 'cover_image', 'banner_image', \
                    'release_format', 'release_status', 'chapters', 'volumes', 'desc', 'average_score', 'mean_score', \
                    'genres', 'synonyms']
            counter = 0

            print('\n')
            print("========================================================================")
            print("============================== MANGA INFO ==============================")
            for key, value in manga_dict.items():
                print(f"{arr[counter]}: {value}")
                counter += 1