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


class QSData:
    '''
    GraphQL Query Strings
    '''
    def __init__(self):
        
        # ===========================
        # ======== | ANIME | ========
        # ===========================
        self.animeInfoQS = """\
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
                }
            }
        """

        # ===========================
        # ======== | MANGA | ========
        # ===========================
        self.mangaInfoQS = """\
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

        # ===========================
        # ======== | STAFF | ========
        # ===========================
        self.staffInfoQS = """\
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

        # ============================
        # ======== | STUDIO | ========
        # ============================
        self.studioInfoQS = """\
            query ($id: Int) {
                Studio(id: $id) {
                    name
                }
            }
        """

        # ============================
        # ====== | CHARACTER | =======
        # ============================
        self.characterInfoQS = """\
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

        # ============================
        # ======== | REVIEW | ========
        # ============================
        self.reviewInfoQS = """\
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

        #=============================================================================
        #/////////////////////////////I Love Emilia///////////////////////////////////
        #=============================================================================


        # ==============================
        # ======== | ANIME ID | ========
        # ==============================
        self.animeIDQS = """\
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
                        coverImage {
                            large
                        }
                        averageScore
                        popularity
                        episodes
                        season
                        hashtag
                        isAdult
                    }
                }
            }
        """

        # =============================
        # ======== | CHAR ID | ========
        # =============================
        self.characterIDQS = """\
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
                        image {
                            large
                        }
                    }
                }
            }
        """

        # ==============================
        # ======== | MANGA ID | ========
        # ==============================
        self.mangaIDQS = """\
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
                        coverImage {
                            large
                        }
                        averageScore
                        popularity
                        chapters
                        volumes
                        season
                        hashtag
                        isAdult
                    }
                }
            }
        """

        # ==============================
        # ======== | STAFF ID | ========
        # ==============================
        self.staffIDQS = """\
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
                        image {
                            large
                        }
                    }
                }
            }
        """

        # ===============================
        # ======== | STUDIO ID | ========
        # ===============================
        self.studioIDQS = """\
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