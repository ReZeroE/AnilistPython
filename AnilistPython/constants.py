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


ANIME_QUERY_FIELDS = [
    "title/romaji",
    "title/english",
    "startDate/year",
    "startDate/month",
    "startDate/day",
    "endDate/year",
    "endDate/month",
    "endDate/day",
    "coverImage/large",
    "bannerImage",
    "format",
    "status",
    "episodes",
    "season",
    "description",
    "averageScore",
    "genres",
    "nextAiringEpisode",
    "isAdult",
    "popularity",
    "countryOfOrigin",
    "duration",
    "updatedAt",
    "source",
    "siteUrl"
]


ANIME_DICT_KEYS = [
    "name_romaji",
    "name_english",
    "starting_time",
    "ending_time",
    "cover_image",
    "banner_image",
    "airing_format",
    "airing_status",
    "airing_episodes",
    "season",
    "desc",
    "average_score",
    "genres",
    "next_airing_ep",
    "is_adult",
    "popularity",
    "origin",
    "duration",
    "updated_at",
    "source",
    "url"
]
















## Anilist APIv2 GraphQL Query Strings 
ANIME_INFO_QUERY = """\
    query ($id: Int) {
        Media(id: $id, type: ANIME) {
            title {
                romaji
                english
            }
            startDate {
                year
                month
                day
            }
            endDate {
                year
                month
                day
            }
            coverImage {
                large
            }
            bannerImage
            format
            status
            episodes
            season
            description
            averageScore
            meanScore
            genres
            synonyms
            nextAiringEpisode {
                airingAt
                timeUntilAiring
                episode
            }
            isAdult
            popularity
            isLicensed
            countryOfOrigin
            duration
            updatedAt
            source
            siteUrl
        }
    }
"""

MANGA_INFO_QUERY = """\
    query ($id: Int) {
        Media(id: $id, type: MANGA) {
            title {
                romaji
                english
            }
            startDate {
                year
                month
                day
            }
            endDate {
                year
                month
                day
            }
            coverImage {
                large
            }
            tags {
                name
            }
            bannerImage
            format
            chapters
            volumes
            status
            description
            averageScore
            meanScore
            genres
            synonyms
        }
    }
"""

STAFF_INFO_QUERY = """\
    query ($id: Int) {
        Staff(id: $id) {
            name {
                first
                last
                native
            }
            description
            language
        }
    }
"""

STUDIO_INFO_QUERY = """\
    query ($id: Int) {
        Studio(id: $id) {
            name
        }
    }
"""

CHARACTER_INFO_QUERY = """\
    query ($id: Int) {
        Character (id: $id) {
            name {
                first
                last
                native
            }
            description
            image {
                large
            }
        }
    }
"""

REVIEW_INFO_QUERY = """\
    query ($id: Int, $html: Boolean) {
        Review (id: $id) {
            summary
            body(asHtml: $html)
            score
            rating
            ratingAmount
            createdAt
            updatedAt
            private
            media {
                id
            }
            user {
                id
                name
                avatar {
                    large
                }
            }
        }
    }
"""


ANIME_ID_QUERY = """\
    query ($query: String, $page: Int, $perpage: Int) {
        Page (page: $page, perPage: $perpage) {
            pageInfo {
                total
                currentPage
                lastPage
                hasNextPage
            }
            media (search: $query, type: ANIME) {
                id
                title {
                    romaji
                    english
                }
            }
        }
    }
"""

CHARACTER_ID_QUERY = """\
    query ($query: String, $page: Int, $perpage: Int) {
        Page (page: $page, perPage: $perpage) {
            pageInfo {
                total
                currentPage
                lastPage
                hasNextPage
            }
            characters (search: $query) {
                id
                name {
                    first
                    last
                }
            }
        }
    }
"""

MANAGA_ID_QUERY = """\
    query ($query: String, $page: Int, $perpage: Int) {
        Page (page: $page, perPage: $perpage) {
            pageInfo {
                total
                currentPage
                lastPage
                hasNextPage
            }
            media (search: $query, type: MANGA) {
                id
                title {
                    romaji
                    english
                }
            }
        }
    }
"""

STAFF_ID_QUERY = """\
    query ($query: String, $page: Int, $perpage: Int) {
        Page (page: $page, perPage: $perpage) {
            pageInfo {
                total
                currentPage
                lastPage
                hasNextPage
            }
            staff (search: $query) {
                id
                name {
                    first
                    last
                }
            }
        }
    }
"""

STUDIO_ID_QUERY = """\
    query ($query: String, $page: Int, $perpage: Int) {
        Page (page: $page, perPage: $perpage) {
            pageInfo {
                total
                currentPage
                lastPage
                hasNextPage
            }
            studios (search: $query) {
                id
                name
            }
        }
    }
"""
