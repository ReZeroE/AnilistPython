"""
Manga-related GraphQL query strings.
"""

class MangaQueries:
    """
    Class containing all manga-related GraphQL queries.
    """
    def __init__(self):
        self.manga_query_by_id = """\
            query ($id: Int) {
                Media(id: $id, type: MANGA) {
                    id
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
                    season
                    hashtag
                    isAdult
                }
            }
        """

        self.manga_query_by_name = """\
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
                        season
                        hashtag
                        isAdult
                    }
                }
            }
        """