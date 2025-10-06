
# MIT License
#
# Copyright (c) 2025 Kevin L.
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


try:
    from .api.anime import Anime
    from .api.character import Character
    from .api.manga import Manga
    from .api.user import User
    from .core.models import AnimeModel, CharacterModel, MangaModel
    from .constants import AUTHOR, VERSION, ANILIST_API_CONFIG

except ImportError:
    from src.api.anime import Anime
    from src.api.character import Character
    from src.api.manga import Manga
    from src.api.user import User
    from src.core.models import AnimeModel, CharacterModel, MangaModel
    from src.constants import AUTHOR, VERSION, ANILIST_API_CONFIG
    

__author__  = AUTHOR
__version__ = VERSION
__all__     = [
    'Anilist',
    'AnimeModel',
    'CharacterModel',
    'MangaModel'
]

class Anilist:
    """
        Initialize a new instance to the Anilist driver API.
        The instance is responsible for all search and retrieve operations. 
        In calls that require a user's auth token, you will need to provide it.
        :ivar dict access: Access required data used through out the program
        :ivar ALAuth auth: Handle Authorization endpoints
    """
    def __init__(self, cid = None, csecret = None, credentials = None):
        
        self.__access_payload = {
            'header': ANILIST_API_CONFIG['HEADERS'],
            'authurl': ANILIST_API_CONFIG['AUTH_URL'],
            'apiurl': ANILIST_API_CONFIG['BASE_URL'],
            'cid': cid,
            'csecret': csecret,
            'token': credentials
        }

        self.anime = Anime(self.__access_payload)
        self.character = Character(self.__access_payload)
        self.manga = Manga(self.__access_payload)
        self.user = User(self.__access_payload)