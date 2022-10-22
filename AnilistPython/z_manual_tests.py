from itertools import count
from __init__ import Anilist
a = Anilist()

import json


# d = a.get_anime("Owari no seraph", manual_select=False)
# # print(d)
# import json
# print(len(d))

# print(json.dumps(d, indent=4))

# print(a.get_anime_id("Code Geass", count=20))
a.print_character_info("C.C", count=5, manual_select=True)