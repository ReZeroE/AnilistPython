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

from tabulate import tabulate

from retrieve_data import ExtractInfo
from retrieve_id import ExtractID
from anilist_exceptions import CharacterNotFoundError, AnilistPythonInternalError

class Character:
    def __init__(self, access_info, activated):
        self.extractInfo = ExtractInfo(access_info, activated)
        self.extractID = ExtractID(access_info, activated)


    def getCharacter(self, character_name, count, manual_select=False) -> dict:
        '''
        Retrieve character info in the form of a json object.
        Retrieve json object will be reformatted in a easily accessable json obj.

        :param character_name: The name of the character
        :return: parsed dict containing the character's data
        :rtype: dict
        '''
        results = []

        character_ids = self.getCharacterIDs(character_name, count, manual_select)
        if len(character_ids) == 0: return results

        for id in character_ids:
            data = self.extractInfo.character(id)
            character = data['data']['Character']

            first_name      = character['name']['first']
            last_name       = character['name']['last']
            native_name     = character['name']['native']
            desc            = character['description']
            image           = character['image']['large']

            character_dict = {
                "first_name": first_name,
                "last_name": last_name,
                "native_name": native_name,
                "desc": desc,
                "image": image
            }
            results.append(character_dict)

        return results


    def getCharacterWithID(self, character_id) -> dict:
        '''
        Retrieve character info in the form of a json object.
        Retrieve json object will be reformatted in a easily accessable json obj.

        :param character_name: The name of the character
        :return: parsed dict containing the character's data
        :rtype: dict
        '''
        data = self.extractInfo.character(character_id)
        character = data['data']['Character']

        first_name      = character['name']['first']
        last_name       = character['name']['last']
        native_name     = character['name']['native']
        desc            = character['description']
        image           = character['image']['large']

        character_dict = {
            "first_name": first_name,
            "last_name": last_name,
            "native_name": native_name,
            "desc": desc,
            "image": image
        }

        return character_dict


    def getCharacterIDs(self, character_name, count, manual_select=False):
        '''
        Retrieves the character ID on Anilist.

        :param character_name: The character of the anime
        :return: The character's ID on Anilist. Returns -1 if an error is caught.
        :rtype: int
        '''

        # ===================================
        # ====== | Manual Select OFF | ======
        # ===================================
        if manual_select == False: 
            character_ids = []
            data = self.extractID.character(character_name, perpage=count)

            try:
                characters_list = data['data']['Page']['characters']
                character_ids = [char['id'] for char in characters_list]
            except IndexError:
                raise CharacterNotFoundError(f'No search result has been found for the anime "{character_name}"!')

            return character_ids


        # ===================================
        # ====== | Manual Select ON | =======
        # ===================================
        elif manual_select == True:
            max_result = 0
            counter = 0 # number of displayed results from search
            data = self.extractID.character(character_name, perpage=count)
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
                    exit(0)

                if user_input > max_result or user_input <= 0:
                    print("Your input does not correspound to any of the characters!")
                    exit(0)
            elif counter == 0:
                raise CharacterNotFoundError(character_name)
            else:
                user_input = 1
            return [data['data']['Page']['characters'][user_input - 1]['id']]


    def displayCharacterInfo(self, character_name, count, manual_select, name_colored):
        '''
        Displays all character data.
        Auto formats the displayed version of the data.

        :param character_name: The character of the anime
        '''
        char_dicts = self.getCharacter(character_name, count, manual_select)
        if len(char_dicts) == 0:
            raise CharacterNotFoundError(character_name)

        data = []
        for char_dict in char_dicts:
            for k, v in char_dict.items():
                if len(str(v)) > 100:
                    v = "<...> (run .get_character() for full view)"
                if v == None or v == "":
                    v = "N/A"
                data.append([k, v])
        
            try:
                print(tabulate(data, tablefmt="fancy_outline"))
            except:
                print(tabulate(data))
            data.clear()
