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
a.update_db()



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

