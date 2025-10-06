"""
Staff and Studio related GraphQL query strings.
"""

class StaffQueries:
    """
    Class containing all staff-related GraphQL queries.
    """
    def __init__(self):
        self.staff_query_by_id = """\
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

        self.staff_query_by_name = """\
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


class StudioQueries:
    """
    Class containing all studio-related GraphQL queries.
    """
    def __init__(self):
        # STUDIO INFO QUERY
        self.studioInfoQS = """\
            query ($id: Int) {
                Studio(id: $id) {
                    name
                }
            }
        """

        # STUDIO ID SEARCH QUERY
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