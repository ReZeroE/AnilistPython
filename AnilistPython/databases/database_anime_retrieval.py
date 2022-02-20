import os
import sys
import json

class DatabaseSearcher:
    def __init__(self):
        self.dir_path = os.path.dirname(os.path.realpath(__file__))
        self.storage_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'anime_database_files')

        self.id_dict_dir = os.path.join(self.storage_dir, "anime_by_id.json")
        self.genre_dict_dir = os.path.join(self.storage_dir, "anime_by_genre.json")
        self.score_dict_dir = os.path.join(self.storage_dir, "anime_by_score.json")
        self.year_dict_dir = os.path.join(self.storage_dir, "anime_by_year.json")



    def anime_mix_search(self, retrieve_count=None, genre=None, year=None, score=None, id_only=False) -> list:
        '''
        Search anime with the given retriction/parameters.

        :param retrieve_count: Max number of anime records to be retrieved. Retrieve all (-1) by default.
        :param genre: The genre of the anime in str or list of str (i.e. 'Action' or ['Action', 'Romance'])
        :param year: The year of the anime in str or list of str (i.e. '2012' or ['2012', '2013'])
        :param score: The score of the anime in str as in range (i.e. '50' or '50-60')
        :param id_only: Only retrieve the ID of the anime. False by default.

        :return: a list of dictionaries containing the anime within the given restrictions.
        :rtype: list
        '''
        if genre == None and year == None and score == None:
            print('Warning -> You have not specified any restrictions (parameters) for this anime search.')
            print("Please use .getAnime(anime_name) if you wish to retrieve an anime's data without any retrictive parameters")
            sys.exit(1)

        options_list = []

        # Genre Restriction
        genre_option_list = []
        if isinstance(genre, str):
            genre_dict = self.load_json(self.genre_dict_dir)
            if genre == 'scifi': genre = 'sci-fi'
            try:
                genre_option_list = genre_dict[genre.strip().lower()]
            except KeyError:
                raise KeyError(f'Incorrect genre category -> {genre.strip().lower()}. For the full genre list, please visit <https://github.com/ReZeroE/AnilistPython>.')

        elif isinstance(genre, list):
            genre_dict = self.load_json(self.genre_dict_dir)

            first = True
            for g in genre:
                if g == 'scifi': g = 'sci-fi'
                try:
                    temp_list = genre_dict[g.strip().lower()]
                except KeyError:
                    raise KeyError(f'Incorrect genre category -> {g.strip().lower()}. For the full genre list, please visit <https://github.com/ReZeroE/AnilistPython>.')

                if first:
                    genre_option_list = temp_list
                    first = False
                else:
                    genre_option_list = list(set(temp_list) & set(genre_option_list))
        elif genre != None:
            print("Error -> paramter genre needs to be a str or list. (i.e. 'Action' or ['Action', 'Romance'])")
            sys.exit(1)


        # Year Retriction
        temp_list = []
        year_option_list = []
        if isinstance(year, int):
            year = str(year)
        if isinstance(year, str):
            year_dict = self.load_json(self.year_dict_dir)
            year_option_list += year_dict[year]
        elif isinstance(year, list):
            if len(year) > 0 and isinstance(year[0], int):
                year = [str(y) for y in year]

            year_dict = self.load_json(self.year_dict_dir)
            for y in year:

                try:
                    temp_list = year_dict[y]
                    year_option_list += year_dict[y]
                except KeyError:
                    raise KeyError(f'Incorrect year value entered -> {y}')


        elif year != None:
            print("Error -> paramter year needs to be a str or list. (i.e. '2012' or ['2012', '2013'])")
            sys.exit(1)


        # Avg Score Striction
        score_option_list = []
        if isinstance(score, int):
            score = str(score)
        if isinstance(score, str):
            score_dict = self.load_json(self.score_dict_dir)

            if score.find('-') != -1:
                min_score = score.split('-')[0]
                max_score = score.split('-')[1]

                try:
                    min_score = int(min_score)
                    max_score = int(max_score)
                except Exception:
                    print(f'parameter score incorrect.')
                    raise Exception

                for key, val in score_dict.items():
                    if int(key) > max_score:
                        break

                    if int(key) > min_score:
                        score_option_list += val
            else:
                try:
                    score_option_list += score_dict[score]
                except Exception:
                    print(f'Parameter score incorrect -> only value 0-100 are accepted')
                    raise Exception
        elif isinstance(score, range):

            min_score = score.start
            max_score = score.stop

            score_dict = self.load_json(self.score_dict_dir)
            for key, val in score_dict.items():
                if int(key) > max_score:
                    break

                if int(key) > min_score:
                    score_option_list += val



        resulting_list = []
        if genre != None and year != None and score != None:
            resulting_list = list(set(genre_option_list) & set(year_option_list) & set(score_option_list))

        elif genre != None and year != None:
            resulting_list = list(set(genre_option_list) & set(year_option_list))
        elif genre != None and score != None:
            resulting_list = list(set(genre_option_list) & set(score_option_list))
        elif year != None and score != None:
            resulting_list = list(set(year_option_list) & set(score_option_list))

        elif genre != None:
            resulting_list = genre_option_list
        elif year != None:
            resulting_list = year_option_list
        elif score != None:
            resulting_list = score_option_list
            
        
        return_list = []

        if id_only == False:
            id_dict = self.load_json(self.id_dict_dir)
            for anime_id in resulting_list:
                return_list.append(id_dict[anime_id])
        else:
            return resulting_list

        return return_list



    def load_json(self, filename):
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data

