# AnilistPython

![example workflow](https://github.com/ReZeroE/AnilistPython/actions/workflows/github-actions-demo.yml/badge.svg)
![downloads](https://img.shields.io/github/workflow/status/ReZeroE/AnilistPython/GitHub%20Actions%20Demo)
![downloads](https://img.shields.io/pypi/dm/AnilistPython)
![licence](https://img.shields.io/github/license/ReZeroE/AnilistPython)
![Test](https://pepy.tech/badge/anilistpython)

AniList Python library (anilist.co APIv2 wrapper) that allows you to **easily search up and retrieve anime, manga, animation studio, and character information.** This library is both beginner-friendly and offers the freedom for more experienced developers to interact with the retrieved information. Provides bot support.

![alt text](https://i.imgur.com/uGzW7vr.jpg)

## Version 0.1.3 Overview
This recent update for AnilistPython has resulted in a moderate change in the library's archetecture for increased efficiency and speed. Various features have also been added to the library. Listed below are some of the main additions and alterations made to the library.

**New features**:
1. Anime search by genre, year, and/or average score (finally!)
2. Offline anime retrieval support for anime - BETA
3. Manga search support
4. Auto setup feature that assist new python programmers to setup the required libraries automatically (auto pre-req lib checking)

Optimization and updates:
1. The lib now has its own prebuild anime database! 
2. Anime, manga, and character search functions have all been optimized, making searches faster!
3. Improved the deepsearch feature in `.get_anime()`. 
4. Manually selecting results feature is now a parameter instead of a seperate function (see usage below). 
 

## How to use?
**Step One:** Library Installation
``` python
pip install AnilistPython==0.1.3
```
**Step Two:** Instance Creation
```python
from AnilistPython import Anilist
anilist = Anilist()
```
**Step Three**: Usage

The AnilistPython library has been split into three distinct sections. Each section has a different set of functions used for retrieving data in that category. Please visit the full documentation for more info or skip to the **General Function Overview** section below for usage.
- **Anime** - ([Documentation](https://github.com/ReZeroE/AnilistPython/wiki/Anime))
- **Manga** - ([Documentation](https://github.com/ReZeroE/AnilistPython/wiki/Manga))
- **Character** - ([Documentation](https://github.com/ReZeroE/AnilistPython/wiki/Character))


## General Function Overview
The following functions are supported by AnilistPyhon version 0.1.3. Only the default parameter has been displayed below. For more information, visit the [full documentation](https://github.com/ReZeroE/AnilistPython/wiki). 
```python
# ANIME
anilist.get_anime("Owari no Seraph")        # returns a dictionary containing info about owari no seraph
anilist.get_anime_with_id(126830)           # returns a dictionary with Code Geass (ID:126830) info 
anilist.get_anime_id("ReZero")              # returns Re:Zero's ID on Anilist
anilist.print_anime_info("Madoka Magica")   # prints all information regarding the anime Madoka Magica

# returns a list of anime with the given restrictions
anilist.search_anime(genre=['Action', 'Adventure', 'Drama'], year=[2016, 2019], score=range(80, 95))

#CHARACTER
anilist.get_character("Emilia")             # returns a dictionary containing the info about Emilia-tan 
anilist.get_character_with_id(13701)        # returns a dictionary with Misaka Mikoto (ID:13701) info
anilist.get_character_id("Milim")           # returns character Milim's ID on Anilist
anilist.print_anime_info("Kirito")          # prints all information regarding the character Kirito

# MANGA
anilist.get_manga("Seraph of the End")      # returns a dictionary containing info about seraph of the end
anilist.get_manga_with_id(113399)           # returns a dictionary with Tearmoon (ID:113399) info
anilist.get_manga_id("Tearmoon Empire")     # returns Tearmoon Empire's ID on Anilist (manga)
anilist.print_manga_info("Tensei Slime")    # prints all information regarding the manga Tensei Slime
```

Note: The feature for manully selecting the top three search results in the terminal is now controlled by a parameter (`manual_select`) in .get functions. For more information, please visit the full documentation. A sample program that has manual select enabled would be:

```python
anilist.get_anime("Owari no Seraph", manual_select=True)
```


## Discord Bot Support
AnilistPython was originially designed to support various Discord Bot features in relation to anime, but throughout the course of its development, more features became available for a wide range of applications other than Discord bots. With that been said, the current version of AnilistPython has further optimized its functions for bot support. From the pre-formatted JSON file upon data retrieval to offline database support (see full documentation), it is now able to be implemented in bots with ease. 

Upcoming AnilistPython Version 0.2.0 will provide functions to generate pre-formated Discord embeds (Anime, Manga, Character embeds) as well as other features that make AnilistPython bot implementations easy to use. 

Sample anime discord bot supported by AnilistPython V0.1.3: [Anime C.C. Discord Bot](https://github.com/ReZeroE/Anime-Discord-Bot)

Note: Please make sure that parameter `manual_select` has not been set to True in bot implementations. (False by default)

## Credits
Lead Developer: Kevin L. (ReZeroE)

Special thanks to the AniList's ApiV2 GraphQL Dev team for making this possible. 
