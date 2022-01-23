# AnilistPython

![example workflow](https://github.com/ReZeroE/AnilistPython/actions/workflows/github-actions-demo.yml/badge.svg)
![downloads](https://img.shields.io/github/workflow/status/ReZeroE/AnilistPython/GitHub%20Actions%20Demo)
![downloads](https://img.shields.io/pypi/dm/AnilistPython)
![licence](https://img.shields.io/github/license/ReZeroE/AnilistPython)
![Test](https://pepy.tech/badge/anilistpython)

AniList Python library (anilist.co APIv2 wrapper) that allows you to **easily search up and retrieve anime, manga, animation studio, and character information.** This library is both beginner-friendly and offers the freedom for more experienced developers to interact with the retrieved information.

![alt text](https://i.imgur.com/uGzW7vr.jpg)

## Upcoming Version 1.1 Overview
This upcoming update for AnilistPython will result in a moderate change in the library's archetecture for increased efficiency and speed. Certain function names have been slightly altered and these changes will be documented properly once the new version is released. In addition to this, The new version will also include prebuilt anime databases to (1) alleviate AniList's APIv2 rate limit issue and (2) Inialize support for offline anime data retrieval

Furthermore, the following new features will be included in the upcoming version:
1. Manga and Anime Studio data retrieval support
2. Anime search by genres, seasons, and/or release years - BETA

I am a full-time uni student so the development on this will be slow. I'will try to push out these new updates once every few months.  

<br/>

## How to use?
**Step One:** Library Installation
``` python
pip install AnilistPython==0.1.0
```
**Step Two:** Instance Creation
```python
from AnilistPython import Anilist
anilist = Anilist()
```
**Step Three**: Usage

Starting off, there are a set of commands optimized for auto json parsing. Currently, they are only available for anime and characters. All of the following functions uses Anilist's new GraphQL API.
```python
# ANIME
anilist.getAnimeInfo("Code Geass")          # returns a dictionary with anime info 
anilist.getAnimeID("ReZero")                # returns Re:Zero's ID on Anilist
anilist.printAnimeInfo("Madoka Magica")     # prints all information regarding the anime Madoka Magica

#CHARACTER
anilist.getCharacterInfo("Emilia")          # returns a dictionary containing the info about Emilia-tan 
anilist.getCharacterID("Milim")             # returns character Milim's ID on Anilist
anilist.printCharacterInfo("Misaka Mikoto") # prints all information regarding the character Misaka Mikoto 
```
Once the commands above are executed, the program will automatically search and retrieve the request information. When multiple targets are found, **three** results will be shown in the terminal. Pick your desired character to retrieve their information.
```ruby
>> anilist.getCharacterInfo("Magica Madoka")

1. Madonna (Movie)
2. Mahou Shoujo Madoka☆Magica
3. Hanoka
Please select the anime that you are searching for in number: <enter 1, 2, or 3>
```

For retrieved dictionaries from by using `.getAnimeInfo()` or `.getCharacterInfo()`, the data would have been parsed and reformatted into more readable and easily accessible json objects. The **keys** to the correspounding dictionaries are as follows:
```ruby
#ANIME DICTIONARY KEYS        #CHARACTER DICTIONARY KEYS
- name_romaji                 - first_name
- name_english                - last_name
- starting_time               - native_name 
- ending_time                 - desc 
- cover_image                 - image
- banner_image
- airing_format
- airing_status
- airing_episodes
- season
- desc
- average_score
- genres
- next_airing_ep
```
One simple example would be:
```crystal
>>> extracted_data = anilist.getAnimeInfo("Tensei Slime")     # retrieves dictionary containing anime data
>>> print(extracted_data["name_romaji"])                      # applies the key "name_romaji"
Tensura Nikki: Tensei Shitara Slime Datta Ken                 # Ta-Da!
```
<br/>

## Sample Program
Sample program that searches up "Sakurasou no Pet na Kanojo". Feel free to copy-paste this into a .py file to test it out!
```python
from AnilistPython import Anilist                            
anilist = Anilist()                                          

data = anilist.getAnimeInfo("Sakurasou")                      

print("Anime Title (Romaji): {name_romaji}".format(**data))   
print("Starting Date: {starting_time}".format(**data))        
print("Ending Date: {ending_time}".format(**data))            
```
<br/>

## Here are some more advanced usages:
(Works for all anime, manga, characters, studio, and staff)

Retrieved data takes the form of json objects or lists of json objects. In order to retrieve the desired data, title/item ID is required. Data extraction does not accept string inputs and can only take int parameters as ID's. The process of chaining ID request and data request together has been included in the optimized functions above, but this is not built-in if you would like to directly request for data blocks in the form or orginial/raw json objects.  

Note that it is possible to directly call functions from the subclasses of the driver code in `ExtractID` and `ExtractInfo` with the Anilist instance.
```python
# RETRIEVING JSON OBJ CONTAINING DATA
anilist.extractInfo.anime(105333)           # Return data on Dr.Stone
anilist.extractInfo.manga(85737)            # Return data on Re:Zero kara Hajimeru Isekai Seikatsu
anilist.extractInfo.staff(103509)           # Return data on Hiroyuki Sawano
anilist.extractInfo.studio(43)              # Return data on ufotable
anilist.extractInfo.review(2113)            # Return review #2113 and format the review body in HTML

# RETRIEVING JSON OBJ CONTAINING ID NUM
anilist.extractID.anime("Owari No Seraph")  # Anime search results for Owari No Seraph.
anilist.extractID.manga("Sakurasou")        # Manga search results for Sakurasou.
anilist.extractID.character("Subaru")       # Character search results for Subaru.
anilist.extractID.staff("Keisuke")          # Staff search results for Keisuke.
anilist.extractID.studio("Ghibli")          # Studio search result for Ghibli.
```
The functions above returns raw json objects that requires extensive parsing before it can be used. Note that `.extractID` does NOT directly return the ID of the given item. Instead, it returns a json object that contains the item's ID number. The only useful information from `.extractID` is the ID number of the provided item. All other data retrieved from `ExtractID` can be found in `ExtractInfo` with the latter having more details.

Parsing the json obj is annoying. For example, if you would like to view the character desc of Rem:
```python
data = anilist.extractID.character("Rem")

for i in range(len(data["data"]["Page"]["characters"])):
    first_name = data["data"]["Page"]["characters"][i]['name']["first"]
    last_name = data["data"]["Page"]["characters"][i]['name']["last"]
    print(f"{first_name}, {last_name}")

user_input = int(input("Select the anime character that you are trying to find: "))
# <checks for corner cases>

info = anilist.extractInfo.character(data['data']['Page']['characters'][user_input - 1]['id'])
print(info["data"]["Character"]["description"])
```
However, worry not! I will be sure to push out more user-friendly functions like the ones I showed at first.

In addition to that, pagination is taken cared of by the new API. By default you retrieve three results but this can be edited to your liking:
```python
extractID(term, page = 1, perpage = 3)
```
<br/>

## Bot Support
The bot support utilizes the features presented above with minor edits for better usability. Currently bot support functions only include anime and character search. Manga search is under development. The file has been completely tested and the test cases are supplied along with the module.

Instance creation for bot functions:
```python
from AnilistPython.botSupport import botSupportClass
anilist_bot = botSupportClass()
```
Usage:
```python
# ANIME
anilist_bot.getAnimeInfo("Demon Slayer")        # returns a dictionary with anime info 
anilist_bot.getAnimeInfoWithID(105333)          # returns a dictionary with anime info - with ID
anilist_bot.getAnimeID("Eighty-Six")            # returns Re:Zero's ID on Anilist

#CHARACTER
anilist_bot.getCharacterInfo("Emilia")          # returns a dictionary containing the info about Emilia-tan 
anilist_bot.getCharacterInfoWithID(93284)       # returns a dictionary containing the info about a character with ID 
anilist_bot.getCharacterID("Milim")             # returns character Milim's ID on Anilist
```
Note that bot support will return the result of the **first match** through searches. If no results are found, Nonetype will be returned for info requests and -1 will be returned for ID request. For more details regarding the functions, please read the in-file comments.

## Credits
Lead Developer: Kevin L. (ReZeroE)

Special thanks to AniList's ApiV2 GraphQL Dev team for making this possible. 
