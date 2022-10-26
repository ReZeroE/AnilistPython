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
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENTgetAnimeIDs. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import datetime
from termcolor import colored
from tabulate import tabulate

from retrieve_data import ExtractInfo
from retrieve_id import ExtractID
from anilist_exceptions import AnimeNotFoundError, AnilistPythonInternalError

class Anime:
    def __init__(self, access_info, activated=True):
        self.extractInfo = ExtractInfo(access_info, activated)
        self.extractID = ExtractID(access_info, activated)


    def getAnime(self, anime_name, count, manual_select=False) -> dict:
        '''
        Retrieve anime info in the form of a JSON object.
        Retrieve JSON object will be reformatted in a easily accessable JSON obj.

        :param anime_name: The name of the anime
        :return: a list of dictionaries containing the anime data
        :rtype: list
        '''
        results = [] # a list of dictionaries with anime data

        ani_ids = self.getAnimeIDs(anime_name, count, manual_select)
        if len(ani_ids) == 0: return results

        for id in ani_ids:
            media = self.extractInfo.anime(id)['data']['Media']

            name_romaji     = media['title']['romaji']
            name_english    = media['title']['english']

            start_year      = media['startDate']['year']
            start_month     = media['startDate']['month']
            start_day       = media['startDate']['day']
            end_year        = media['endDate']['year']
            end_month       = media['endDate']['month']
            end_day         = media['endDate']['day']
            starting_time   = f'{start_month}/{start_day}/{start_year}'
            ending_time     = f'{end_month}/{end_day}/{end_year}'

            cover_image     = media['coverImage']['large']
            banner_image    = media['bannerImage']
            airing_format   = media['format']
            airing_status   = media['status']
            airing_episodes = media['episodes']
            season          = media['season']
            desc            = media['description']
            average_score   = media['averageScore']
            genres          = media['genres']
            next_airing_ep  = media['nextAiringEpisode']
            is_adult        = media['isAdult']
            popularity      = media['popularity']
            origin          = media['countryOfOrigin']
            duration        = media['duration']
            updated_at      = media['updatedAt']
            source          = media['source']
            url             = media['siteUrl']

            anime_dict = {
                "name_romaji"       : name_romaji,
                "name_english"      : name_english,
                "starting_time"     : starting_time,
                "ending_time"       : ending_time,
                "cover_image"       : cover_image,
                "banner_image"      : banner_image,
                "airing_format"     : airing_format,
                "airing_status"     : airing_status,
                "airing_episodes"   : airing_episodes,
                "season"            : season,
                "desc"              : desc,
                "average_score"     : average_score,
                "genres"            : genres,
                "next_airing_ep"    : next_airing_ep,
                "is_adult"          : is_adult,
                "popularity"        : popularity,
                "origin"            : origin,
                "duration"          : duration,
                "updated_at"        : updated_at,
                "source"            : source,
                "url"               : url
            }

            results.append(anime_dict)

        return results


    def getAnimeWithID(self, anime_id) -> dict:
        '''
        Retrieve anime info in the form of a JSON object.
        Retrieve JSON object will be reformatted in a easily accessable JSON obj.

        :param anime_name: The name of the anime
        :return: parsed dict containing the anime's data
        :rtype: dict
        '''

        data = self.extractInfo.anime(anime_id)
        media = data['data']['Media']

        name_romaji     = media['title']['romaji']
        name_english    = media['title']['english']

        start_year      = media['startDate']['year']
        start_month     = media['startDate']['month']
        start_day       = media['startDate']['day']
        end_year        = media['endDate']['year']
        end_month       = media['endDate']['month']
        end_day         = media['endDate']['day']
        starting_time   = f'{start_month}/{start_day}/{start_year}'
        ending_time     = f'{end_month}/{end_day}/{end_year}'

        cover_image     = media['coverImage']['large']
        banner_image    = media['bannerImage']
        airing_format   = media['format']
        airing_status   = media['status']
        airing_episodes = media['episodes']
        season          = media['season']
        desc            = media['description']
        average_score   = media['averageScore']
        genres          = media['genres']
        next_airing_ep  = media['nextAiringEpisode']
        is_adult        = media['isAdult']
        popularity      = media['popularity']
        origin          = media['countryOfOrigin']
        duration        = media['duration']
        updated_at      = media['updatedAt']
        source          = media['source']
        url             = media['siteUrl']

        anime_dict = {
            "name_romaji"       : name_romaji,
            "name_english"      : name_english,
            "starting_time"     : starting_time,
            "ending_time"       : ending_time,
            "cover_image"       : cover_image,
            "banner_image"      : banner_image,
            "airing_format"     : airing_format,
            "airing_status"     : airing_status,
            "airing_episodes"   : airing_episodes,
            "season"            : season,
            "desc"              : desc,
            "average_score"     : average_score,
            "genres"            : genres,
            "next_airing_ep"    : next_airing_ep,
            "is_adult"          : is_adult,
            "popularity"        : popularity,
            "origin"            : origin,
            "duration"          : duration,
            "updated_at"        : updated_at,
            "source"            : source,
            "url"               : url
        }

        return anime_dict


    def getAnimeIDs(self, anime_name, count, manual_select=False):
        '''
        Retrieves the anime ID on Anilist.

        :param anime_name: The name of the anime
        :return: The anime's ID on Anilist. Returns -1 if an error is caught.
        :rtype: list
        '''
        # ===================================
        # ====== | Manual Select OFF | ======
        # ===================================
        if manual_select == False:
            data = self.extractID.anime(anime_name, perpage=count)
            anime_ids = []
            try:
                # anime_ID = data['data']['Page']['media'][0]['id']
                for anime_media in data['data']['Page']['media']:
                    anime_ids.append(anime_media['id'])
            except IndexError:
                raise AnimeNotFoundError(anime_name)
            return anime_ids

        # ===================================
        # ====== | Manual Select ON | =======
        # ===================================
        elif manual_select == True:
            data = self.extractID.anime(anime_name, perpage=count)
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
                    exit(0)
                if user_input > max_result or user_input <= 0:
                    print("Your input does not correspound to any of the anime displayed!")
                    exit(0)
            elif counter == 0:
                raise AnimeNotFoundError(anime_name)
            else:
                user_input = 1
            return [data['data']['Page']['media'][user_input - 1]['id']]

    def displayAnimeInfo(self, anime_name, count, manual_select, title_colored):
        '''
        Displays all anime data in a fancy table.
        Auto formats the displayed version of the data.

        :param anime_name: The name of the anime
        '''
        ani_dicts = self.getAnime(anime_name, count, manual_select)
        if len(ani_dicts) == 0: 
            raise AnimeNotFoundError(anime_name)

        data_list = []
        for ani_dict in ani_dicts:
            for k, v in ani_dict.items():
                if k == 'name_romaji' or k == 'name_english' and title_colored:
                    v = colored(v, "cyan")
                if len(str(v)) > 100:
                    v = "<...> (run .get_anime() for full view)"
                elif v == None:
                    v = "N/A"
                elif k == "updated_at":
                    try:
                        v = str(datetime.datetime.fromtimestamp(int(v)))
                    except ValueError:
                        pass
                elif k == "duration":
                    v = f"{v} minutes"
                data_list.append([k, v])

            print(tabulate(data_list, tablefmt="fancy_outline"))
            data_list.clear()