
from unittest import result
import numpy as np
import time
import json
import os


class SearchEngine:
    def __init__(self):
        self.dir_path = os.path.dirname(os.path.realpath(__file__))
        self.storage_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'anime_database_files')

        self.id_dict_dir = os.path.join(self.storage_dir, "anime_by_id.json")
        self.id_cache_dict_dir = os.path.join(self.storage_dir, "anime_by_id_cache.json")
        self.tag_dict_dir = os.path.join(self.storage_dir, "anime_by_tag.json")
        self.tag_cache_dict_dir = os.path.join(self.storage_dir, "anime_by_tag_cache.json")

        self.cache_size = 500

    def search_anime_database(self, anime_name, accuracy_threshold=0.7, full_record_override=False):
        tag_dict = self.load_json(self.tag_dict_dir)

        resulting_dict = dict()
        caching_dict = self.load_json(self.tag_cache_dict_dir)
        caching_queue = []

        ini_len = len(resulting_dict)

        # searches the cached database
        import copy
        temp_caching_dict = copy.deepcopy(caching_dict)
        if full_record_override == False:
            for anime_tag, anime_id in temp_caching_dict.items():
                curr_tags = ['ph']
                if anime_tag.find('|=|') != -1:
                    curr_tags = anime_tag.split('|=|')
                    curr_tags = [tag.lower() for tag in curr_tags]
                else:
                    curr_tags[0] = anime_tag.lower()

                for tag in curr_tags:
                    acc = self.levenshtein_ratio(anime_name, tag, ratio_calc=True)
                    if acc >= accuracy_threshold:
                        resulting_dict[anime_id] = acc

                        if len(curr_tags) == 1:
                            caching_dict[curr_tags[0]] = anime_id
                        else:
                            caching_dict[f'{curr_tags[0]}|=|{curr_tags[1]}'] = anime_id


        # searches record from the master database if
        #   - cache search record len < 2 
        #   (OR)
        #   - full_record_override is on
        if len(resulting_dict) - ini_len < 2 or full_record_override == True:
            for anime_tag, anime_id in tag_dict.items():
                curr_tags = ['ph']
                if anime_tag.find('|=|') != -1:
                    curr_tags = anime_tag.split('|=|')
                    curr_tags = [tag.lower() for tag in curr_tags]
                else:
                    curr_tags[0] = anime_tag.lower()

                for tag in curr_tags:
                    acc = self.levenshtein_ratio(anime_name, tag, ratio_calc=True)
                    if acc >= accuracy_threshold:
                        resulting_dict[anime_id] = acc

                        if len(curr_tags) == 1:
                            caching_dict[curr_tags[0]] = anime_id
                        else:
                            caching_dict[f'{curr_tags[0]}|=|{curr_tags[1]}'] = anime_id

        resulting_dict = dict(sorted(resulting_dict.items(), key=lambda item: item[1], reverse=True))


        # queue the record for removal if cache size > max allowed cache size
        if len(caching_queue) > self.cache_size:
            for k, v in caching_dict.items():
                caching_queue.append({k : v})

            while len(caching_queue) > self.cache_size:
                caching_queue.pop(0)

            caching_dict.clear()
            for d in caching_queue:
                caching_dict.update(d)

        # load data to the cache database
        with open(self.tag_cache_dict_dir, 'w') as wf:
            json.dump(caching_dict, wf, indent=4)

        
        resulting_list = []
        id_dict = self.load_json(self.id_dict_dir)
        for anime_id, acc in resulting_dict.items():
            resulting_list.append(id_dict[anime_id])

        return resulting_list

    def levenshtein_ratio(self, s, t, ratio_calc = False):
        '''
            levenshtein_ratio_and_distance:
            Calculates levenshtein distance between two strings.
            If ratio_calc = True, the function computes the
            levenshtein distance ratio of similarity between two strings
            For all i and j, distance[i,j] will contain the Levenshtein
            distance between the first i characters of s and the
            first j characters of t
        '''


        if t.find(s) != -1:
            return 1.01 # name contains enterned characters

        rows = len(s)+1
        cols = len(t)+1
        distance = np.zeros((rows,cols),dtype = int)
        for i in range(1, rows):
            for k in range(1,cols):
                distance[i][0] = i
                distance[0][k] = k
    
        for col in range(1, cols):
            for row in range(1, rows):
                if s[row-1] == t[col-1]:
                    cost = 0 
                else:
                    if ratio_calc == True:
                        cost = 2
                    else:
                        cost = 1
                distance[row][col] = min(distance[row-1][col] + 1, 
                                    distance[row][col-1] + 1, 
                                    distance[row-1][col-1] + cost)  
        if ratio_calc == True:
            Ratio = ((len(s)+len(t)) - distance[row][col]) / (len(s)+len(t))
            return Ratio
        else:
            return "The strings are {} edits away".format(distance[row][col])

    def load_json(self, filename):
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data

    def reverse_dict(self, d):
        return {value : key for (key, value) in d.items()}

if __name__ == '__main__':
    import time
    start = time.time()
    se = SearchEngine()
    se.search_anime_database('react', accuracy_threshold=0.7)
    print(time.time() - start)