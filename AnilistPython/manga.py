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



from termcolor import colored
from tabulate import tabulate

from retrieve_data import ExtractInfo
from retrieve_id import ExtractID
from anilist_exceptions import MangaNotFoundError

class Manga:
    def __init__(self, access_info, activated=True):
        self.extractInfo = ExtractInfo(access_info, activated)
        self.extractID = ExtractID(access_info, activated)


    def getManga(self, manga_name, count, manual_select=False):
        '''
        Retrieve character info in the form of a json object.
        Retrieve json object will be reformatted in a easily accessable json obj.

        :param character_name: The name of the character
        :return: parsed dict containing the character's data
        :rtype: dict
        '''
        results = []

        manga_ids = self.getMangaIDs(manga_name, count, manual_select)
        if len(manga_ids) == 0: return results

        for manga_id in manga_ids:

            data = self.extractInfo.manga(manga_id)
            media = data['data']['Media']
            
            name_romaji     = media['title']['romaji']
            name_english    = media['title']['english']

            start_year      = media['startDate']['year']
            start_month     = media['startDate']['month']
            start_day       = media['startDate']['day']
            end_year        = media['endDate']['year']
            end_month       = media['endDate']['month']
            end_day         = media['endDate']['day']

            starting_time = f'{start_month}/{start_day}/{start_year}'
            ending_time = f'{end_month}/{end_day}/{end_year}'

            cover_image     = media['coverImage']['large']
            banner_image    = media['bannerImage']
            release_format  = media['format']
            release_status  = media['status']
            chapters        = media['chapters']
            volumes         = media['volumes']
            desc            = media['description']
            average_score   = media['averageScore']
            mean_score      = media['meanScore']
            genres          = media['genres']
            synonyms        = media['synonyms']

            manga_dict = {
                "name_romaji": name_romaji,
                "name_english": name_english,
                "starting_time": starting_time,
                "ending_time": ending_time,
                "cover_image": cover_image,
                "banner_image": banner_image,
                "release_format": release_format,
                "release_status": release_status,
                "chapters": chapters,
                "volumes": volumes,
                "desc": desc,
                "average_score": average_score,
                "mean_score": mean_score,
                "genres": genres,
                "synonyms": synonyms
            }
            results.append(manga_dict)

        return results


    def getMangaWithID(self, manga_id) -> dict:
        '''
        Retrieve character info in the form of a json object.
        Retrieve json object will be reformatted in a easily accessable json obj.

        :param character_name: The name of the character
        :return: parsed dict containing the character's data
        :rtype: dict
        '''

        data = self.extractInfo.manga(manga_id)
        media = data['data']['Media']
        
        name_romaji     = media['title']['romaji']
        name_english    = media['title']['english']

        start_year      = media['startDate']['year']
        start_month     = media['startDate']['month']
        start_day       = media['startDate']['day']
        end_year        = media['endDate']['year']
        end_month       = media['endDate']['month']
        end_day         = media['endDate']['day']

        starting_time = f'{start_month}/{start_day}/{start_year}'
        ending_time = f'{end_month}/{end_day}/{end_year}'

        cover_image     = media['coverImage']['large']
        banner_image    = media['bannerImage']
        release_format  = media['format']
        release_status  = media['status']
        chapters        = media['chapters']
        volumes         = media['volumes']
        desc            = media['description']
        average_score   = media['averageScore']
        mean_score      = media['meanScore']
        genres          = media['genres']
        synonyms        = media['synonyms']

        manga_dict = {
            "name_romaji": name_romaji,
            "name_english": name_english,
            "starting_time": starting_time,
            "ending_time": ending_time,
            "cover_image": cover_image,
            "banner_image": banner_image,
            "release_format": release_format,
            "release_status": release_status,
            "chapters": chapters,
            "volumes": volumes,
            "desc": desc,
            "average_score": average_score,
            "mean_score": mean_score,
            "genres": genres,
            "synonyms": synonyms
        }

        return manga_dict

    def getMangaIDs(self, manga_name, count, manual_select=False):
        '''
        Retrieves the character ID on Anilist.

        :param character_name: The character of the Manga
        :return: The character's ID on Anilist. Returns -1 if an error is caught.
        :rtype: int
        '''

        # ===================================
        # ====== | Manual Select OFF | ======
        # ===================================
        if manual_select == False:
            manga_ids= []
            data = self.extractID.manga(manga_name, perpage=count)
            try:
                for media in data['data']['Page']['media']:
                    manga_ids.append(media['id'])
            except IndexError:
                raise MangaNotFoundError(manga_name)

            return manga_ids


        # ===================================
        # ====== | Manual Select ON | =======
        # ===================================
        elif manual_select == True:
            max_result = 0
            counter = 0 # number of displayed results from search
            data = self.extractID.manga(manga_name, perpage=count)
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
                    exit(0)
                if user_input > max_result or user_input <= 0:
                    print("Your input does not correspound to any of the manga displayed!")
                    exit(0)
            elif counter == 0:
                print(f'No search result has been found for the manga "{manga_name}"!')
                exit(0)
            else:
                user_input = 1

            return [data['data']['Page']['media'][user_input - 1]['id']]

    def displayMangaInfo(self, manga_name, count, manual_select, title_colored):
        '''
        Displays all character data.
        Auto formats the displayed version of the data.

        :param character_name: The character of the Manga
        '''

        manga_dicts = self.getManga(manga_name, count, manual_select)
        if len(manga_dicts) == 0:
            raise MangaNotFoundError(manga_name)
        
        data_list = []
        for manga_dict in manga_dicts:
            for k, v in manga_dict.items():
                if k == 'name_romaji' or k == 'name_english' and title_colored:
                    v = colored(v, "cyan")
                if len(str(v)) > 100:
                    v = "<...> (run .get_anime() for full view)"
                if k == 'genres' or k == "synonyms":
                    v = ", ".join(v)
                elif v == None:
                    v = "N/A"
                data_list.append([k, v])

            try:
                print(tabulate(data_list, tablefmt="fancy_outline"))
            except:
                print(tabulate(data_list))
            data_list.clear()