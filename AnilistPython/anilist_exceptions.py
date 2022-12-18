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


class AnimeNotFoundError(Exception):
    __module__ = 'builtins'
    def __init__(self, anime_name):
        self.message = f"\nf'No search result has been found for the anime `{anime_name}`."
        super().__init__(self.message)


class CharacterNotFoundError(Exception):
    __module__ = 'builtins'
    def __init__(self, character_name):
        self.message = f"\nf'No search result has been found for the character `{character_name}`."
        super().__init__(self.message)


class MangaNotFoundError(Exception):
    __module__ = 'builtins'
    def __init__(self, manga_name):
        self.message = f"\nf'No search result has been found for the manga `{manga_name}`."
        super().__init__(self.message)


class AnilistPythonInternalError(Exception):
    __module__ = 'builtins'
    def __init__(self, message="AnilistPython Internal Error Has Occurred."):
        self.message = message
        super().__init__(self.message)


class AnilistPythonDSError(Exception):
    __module__ = 'builtins'
    def __init__(self, message="AnilistPython Deep Search Error Has Occurred. Try setting deep_search in .get_anime() to False."):
        self.message = message
        super().__init__(self.message)
