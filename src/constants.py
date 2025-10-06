# SPDX-License-Identifier: MIT
# MIT License
#
# Copyright (c) 2024 Kevin L.
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

# =========================================
# ==========| MODULE CONSTANTS | ==========
# =========================================

BASENAME            = "AnilistPython"
SHORTNAME           = "AnilistPython"
COMMAND             = "anilist"
VERSION             = "1.0.0"
VERSION_DESC        = "Stable"

AUTHOR              = "Kevin L."
AUTHOR_DETAIL       = f"{AUTHOR} - kevinliu@vt.edu - Github: ReZeroE"
REPOSITORY          = "https://github.com/ReZeroE/AnilistPython"
BUG_TRACKER         = f"{REPOSITORY}/issues"

TIME_FORMAT         = "%H:%M:%S"
DATETIME_FORMAT     = "%Y-%m-%d %H:%M:%S"

# =========================================
# =========| API CONFIGURATION | ==========
# =========================================
    
ANILIST_API_CONFIG = {
    "DOC_URL": "https://docs.anilist.co/",
    "BASE_URL": "https://graphql.anilist.co",
    "AUTH_URL": "https://anilist.co/api",
    "HEADERS": {
        "Content-Type": "application/json",
        "User-Agent": "AnilistPython (github.com/ReZeroE/AnilistPython)",
        "Accept": "application/json"
    }
}

# =========================================
# ===========| ERROR MESSAGES | ===========
# =========================================

ERROR_MESSAGES = {
    "ANIME_NOT_FOUND": "Anime Not Found",
    "CHARACTER_NOT_FOUND": "Character Not Found", 
    "MANGA_NOT_FOUND": "Manga Not Found",
    "INVALID_GENRE": "Incorrect genre category -> {}. For the full genre list, please visit <{}>.",
    "INVALID_INPUT": "Your input is incorrect! Please try again!",
    "INPUT_OUT_OF_RANGE": "Your input does not correspound to any of the anime displayed!",
    "NO_SEARCH_RESULT": 'No search result has been found for the anime "{}"!',
    "DATA_POST_UNSUCCESSFUL": "Data post unsuccessful. ({})",
    "FUNCTION_DISABLED": "Current function status is False."
}