"""
Character-related GraphQL query strings.
"""

class CharacterQueries:
    """
    Class containing all character-related GraphQL queries.
    """
    def __init__(self):
        self.character_query_by_id = """\
            query ($id: Int) {
                Character (id: $id) {
                    id
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

        self.character_query_by_name = """\
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
                            native
                        }
                        description
                        image {
                            large
                        }
                    }
                }
            }
        """