from itertools import count
from __init__ import Anilist, AnimeDB
anilist  = Anilist()
anime_db = AnimeDB()

ani_list = anilist.print_anime_info("no game no life", count=1)
print(ani_list)