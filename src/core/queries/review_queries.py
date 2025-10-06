"""
Review-related GraphQL query strings.
"""

class ReviewQueries:
    """
    Class containing all review-related GraphQL queries.
    """
    def __init__(self):
        self.review_query_by_id = """\
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