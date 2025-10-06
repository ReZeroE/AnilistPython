"""
Anime-related GraphQL query strings.
"""

class AnimeQueries:
    """
    Class containing all anime-related GraphQL queries.
    """
    def __init__(self):
        self.anime_query_by_id = """\
            query ($id: Int) {
                Media(id: $id, type: ANIME) {
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

        self.anime_query_by_name = """\
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
            }
        """