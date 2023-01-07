



# AnilistPython

![example workflow](https://github.com/ReZeroE/AnilistPython/actions/workflows/github-actions-demo.yml/badge.svg)
![downloads](https://img.shields.io/pypi/dm/AnilistPython)
![licence](https://img.shields.io/github/license/ReZeroE/AnilistPython)
![Test](https://pepy.tech/badge/anilistpython)

AniList Python library (anilist.co APIv2 wrapper) that allows you to easily **look up and retrieve anime, manga, and character information in Python**. This beginner-friendly library provides the perfect toolkits to support anime/manga Discord bots and other related software applications. MIT licensed.

![alt text](https://i.imgur.com/uGzW7vr.jpg)

## Version 1.0.0 Overview (Stable Release)
AnilistPython v1.0.0 is the first stable release of the AnilistPython library. (Finally!)

In this release, a number of previous features have been updated and optimized for efficiency and modularity. A handful of new features have been also added to the library as well. The current version of AnilistPython has two submodules (Anilist and AnimeDB), supporting both online and offline data look up and retrieval.

```
Anilist (supported by Anilist APIv2)
  - Anime
      - Search by id
      - Search by name
          - normal/deepsearch
      - Terminal support (print anime info) 
  - Manga
      - Search by id
      - Search by name
      - Terminal support (print managa info)
  - Character
      - Search by id
      - Search by name
      - Terminal support (print character info)

AnimeDB
  - Anime
    - Search by id
    - Search by name
    - Search by release year
    - Search by season
    - Utility functions (database update)
```
 

## Installation
Library Installation From [PyPI](https://pypi.org/project/AnilistPython/):
``` python
pip install AnilistPython==1.0.0
or
pip3 install AnilistPython==1.0.0
```




## Usage Overview
The AnilistPython library contains submodules. **(1) Anilist** supports online information lookup for Anime, Manga, and Character through the use of anilist.co APIv2. **(2) AnimeDB** supports offline information lookup for only anime, but offers number of functions for better data filtering.

- **1. Anilist** (Online)
   - Anime - ([Documentation](https://github.com/ReZeroE/AnilistPython/wiki/Anime))
   - Manga - ([Documentation](https://github.com/ReZeroE/AnilistPython/wiki/Manga))
   - Character - ([Documentation](https://github.com/ReZeroE/AnilistPython/wiki/Character))
   
- **2. AnimeDB** (Offline)
     - Anime - ([Documentation](https://github.com/ReZeroE/AnilistPython/wiki/Anime))
     

***


### 1. Anilist
```python
from AnilistPython import Anilist
anilist = Anilist()
```
#### - Anime
```python
# ANIME
anilist.get_anime("Owari no Seraph")        # returns a list of anime dictionaries about Owari no Seraph
anilist.get_anime_with_id(126830)           # returns a dictionary with Code Geass' (ID:126830) info 
anilist.get_anime_id("ReZero")              # returns Re:Zero's ID(s) on Anilist
anilist.print_anime_info("Madoka Magica")   # prints all information regarding the anime Madoka Magica
```

#### - Manga
```python
# MANGA
anilist.get_manga("Eighty Six")             # returns a list of Eighty-Six managa dictionaries
anilist.get_manga_with_id(113399)           # returns a dictionary with Tearmoon's (ID:113399) info
anilist.get_manga_id("Tearmoon Empire")     # returns Tearmoon Empire's ID(s) on Anilist (manga)
anilist.print_manga_info("Tensei Slime")    # prints all information regarding the manga Tensei Slime
```

#### - Character
```python
#CHARACTER
anilist.get_character("Emilia")             # returns a list of Emilia-tan dictionaries 
anilist.get_character_with_id(13701)        # returns a dictionary with Misaka Mikoto's (ID:13701) info
anilist.get_character_id("Milim")           # returns character Milim's ID(s) on Anilist
anilist.print_anime_info("Kirito")          # prints all information regarding the character Kirito
```

***

### 2. AnimeDB 
As the name suggests, AnilistPython's AnimeDB submodule supports **OFFLINE** anime data look up and retrieval. 
```python
from AnilistPython import AnimeDB
anime_db = AnimeDB(auto_update=True)
```
#### - Search by anime ID
```python
# Search anime with ID:138161
anime_db.search_by_id(138161)
```
#### - Search by anime name
```python
# Search anime with name Re:Zero
anime_db.search_by_name("Re:Zero")
anime_db.search_by_name("Re:Zero", id_only=True, case_sensitive=True)
```

#### - Search by anime's release year(s)
```python
# Search anime with a release year of 2019
anime_db.search_by_release_year(2019)
anime_db.search_by_release_year(2019, id_only=True)

# Search anime with a release year BETWEEN 2018 and 2022 (inclusive)
anime_db.search_by_release_year(range(2018, 2022))
anime_db.search_by_release_year(range(2018, 2022), id_only=True)

# Search anime with a release year of 2018 OR 2020 
anime_db.search_by_release_year([2018, 2020])
anime_db.search_by_release_year([2018, 2020], id_only=True)
```

#### - Search by anime's genre(s)
```python
# Search anime with generes mahou shoujo AND drama
anime_db.search_by_genre(['mahou shoujo', 'drama'])
anime_db.search_by_genre(['mahou shoujo', 'drama'], id_only=True)
```
#### - Search by anime's season
```python
# Search anime with a release season of Spring
anime_db.search_by_season("spring")
anime_db.search_by_season("spring", id_only=True)
```

#### - Utility: Update DB
```python
# Download the newest DB from Github
anime_db.update_db()
anime_db.update_db(verbose=False)
```

***

## Sample Programs
#### Sample Program 1: Simple anime lookup for the name Re:Zero
```python
from AnilistPython import Anilist
anilist = Anilist()

# Search anime "Re:Zero" for 3 matching results
res = anilist.get_anime("Re:Zero", count=3)

# Get first result (res is a list)
first_result = res[0]

# Print the anime's name in Romaji, its starting/ending times, and its popularity
print(first_result['name_romaji'])
print(first_result['starting_time'])
print(first_result['ending_time'])
print(first_result['popularity'])
```
```
STDOUT:
Re:Zero kara Hajimeru Isekai Seikatsu
4/4/2016
9/19/2016
366192
```

#### Sample Program 2: Search anime with the following restrictions:

- Released between **2019 - 2023**
- Released in the season **Fall**
- Must have the genre labels: **mystery, drama, and adventure**

Note: Anime lookup with data filtering is only supported by AnimeDB, thus we need to use AnimeDB for lookup. 

```python
from AnilistPython import Anilist, AnimeDB
anilist  = Anilist()
anime_db = AnimeDB()

# Get the anime IDs that satisfy each restriction
res_year    = anime_db.search_by_release_year(range(2019, 2023), id_only=True)
res_season  = anime_db.search_by_season("Fall", id_only=True)
res_genre   = anime_db.search_by_genre(["mystery", "drama", "adventure"], id_only=True)

# Find the intersection between the three lists of IDs to get the anime that satisfy all three conditions
req_satisfied_ids = list(set(res_year) & set(res_season) & set(res_genre))

# Get anime data with the IDs from Anilist
for anime_id in req_satisfied_ids:
    print(anilist.get_anime_with_id(anime_id))
```

If an error occurs while running AnilistPython, please refer the to the [Error Fixes](https://github.com/ReZeroE/AnilistPython#error-fixes) section.

## Discord Bot Support
Sample anime discord bot supported by AnilistPython V0.1.3: [Anime C.C. Discord Bot](https://github.com/ReZeroE/Anime-Discord-Bot)


## License

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/MIT_logo.svg/220px-MIT_logo.svg.png" align="left" width="150"/>

<ul>
 - MIT Licensed
</ul>

<br clear="left"/>


## Credits
Lead Developer: Kevin L. (ReZeroE)

Special thanks to the AniList's ApiV2 GraphQL Dev team for making this possible. 
