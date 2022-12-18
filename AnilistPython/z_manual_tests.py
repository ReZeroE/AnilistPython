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
# a.print_manga_info("tearoom empire", count=5, manual_select=True)
# a.update_db()

# a.print_manga_info("86", manual_select=True, count=5)


# access = {'header': {'Content-Type': 'application/json',
#                             'User-Agent': 'AnilistPython (github.com/ReZeroE/AnilistPython)',
#                             'Accept': 'application/json'},
#                     'authurl': 'https://anilist.co/api',
#                     'apiurl': 'https://graphql.anilist.co',
#                     'cid': None,
#                     'csecret': None,
#                     'token': None}

# print(a.get_anime_with_id(21765))


from __init__ import AnimeDatabase
a = AnimeDatabase()

print(a.update_db())


# from retrieve_id import ExtractID
# e = ExtractID(access=access, status=True)

# print(e.manga("tearmoon"))


# from retrieve_data import ExtractInfo
# d = ExtractInfo(access, True)

# print(d.manga(112830))

# from github import Github
# g = Github()

# repo = g.get_repo("ReZeroE/AnilistPython")
# commits = repo.get_commits(path='AnilistPython/databases/')
# print(commits.totalCount)
# for i in range(commits.totalCount):
#     print(commits[i].commit.sha)
# if commits.totalCount:
#     print(commits[0].commit.committer.date)

# com = repo.get_commit(sha="4b310a9263753f96cc8b87bbc762180a25624819")
# print(com.commit.author.date)

