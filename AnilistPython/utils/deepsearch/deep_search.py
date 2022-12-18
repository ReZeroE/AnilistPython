# SPDX-License-Identifier: MIT
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


import re

from ..anilist_translator.translate import AnilistPythonTranslate
from anilist_exceptions import AnilistPythonDSError

class DeepSearch():
    '''
    Translation wrapper module that offers more accurate search/retrieval results Currently in BETA testing phase.
    '''
    def __init__(self):
        pass

    def deep_search_name_conversion(self, anime_name) -> str:
        '''
        Function for converting the name of the anime into Japanese using the built-in Google translator.
        Note: this is an optional function due to its instability (translation failures).

        :param anime_name: the name of the anime to be searched
        :rtype: str
        '''
        try:
            translator = AnilistPythonTranslate(source='english', target='japanese')
            anime_name_jp = translator.translate(f'{anime_name} anime')
        except:
            raise AnilistPythonDSError()

        anime_name_final = anime_name_jp.replace(' ', '').replace('アニメ', '')

        # Translation Ineffective
        if re.search('^[a-zA-Z]*$', anime_name_final) != None:
            return anime_name
        
        return anime_name_final
