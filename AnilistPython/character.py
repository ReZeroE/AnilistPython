import time
import requests
from .retrieve_data import ExtractInfo
from .retrieve_id import ExtractID

class Character:
    def __init__(self, access_info, activated):
        self.extractInfo = ExtractInfo(access_info, activated)
        self.extractID = ExtractID(access_info, activated)


    def getCharacter(self, character_name, manual_select=False) -> dict:
        '''
        Retrieve character info in the form of a json object.
        Retrieve json object will be reformatted in a easily accessable json obj.

        :param character_name: The name of the character
        :return: parsed dict containing the character's data
        :rtype: dict
        '''

        character_id = self.getCharacterID(character_name, manual_select)
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


    def getCharacterWithID(self, character_id) -> dict:
        '''
        Retrieve character info in the form of a json object.
        Retrieve json object will be reformatted in a easily accessable json obj.

        :param character_name: The name of the character
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


    def getCharacterID(self, character_name, manual_select=False):
        '''
        Retrieves the character ID on Anilist.

        :param character_name: The character of the anime
        :return: The character's ID on Anilist. Returns -1 if an error is caught.
        :rtype: int
        '''

        # if manual select is turned off ============================================================================
        if manual_select == False: 
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


        # if manual select is turned on =============================================================================
        elif manual_select == True:
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

        else:
            # placeholder
            pass


    def displayCharacterInfo(self, character_name, manual_select=False):
        '''
        Displays all character data.
        Auto formats the displayed version of the data.

        :param character_name: The character of the anime
        '''

        char_dict = self.getCharacter(character_name, manual_select)
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