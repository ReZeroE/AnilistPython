"""
User-related GraphQL query strings.
"""

class UserQueries:
    """
    Class containing all user-related GraphQL queries.
    """
    def __init__(self):
        # GET AUTHENTICATED CURRENT USER ID
        self.user_query = """\
            query{
	            Viewer{
		            id
	            }
            }
        """

        self.user_activity_query_by_id = """\
            query($id:Int,$type:ActivityType,$page:Int,$perPage: Int){
                Page(page:$page,perPage:$perPage){
                    pageInfo{
                        total
                        perPage
                        currentPage
                        lastPage
                        hasNextPage
                    }
                    activities(userId:$id,type:$type,sort:[PINNED,ID_DESC]){
                    ... on ListActivity{
                        id
                        type
                        replyCount
                        status
                        progress
                        isLocked
                        isSubscribed
                        isLiked
                        isPinned
                        likeCount
                        createdAt
                        user{
                            id
                            name
                            avatar{
                                large
                            }
                        }
                        media{
                            id
                            type
                            status(version:2)
                            isAdult
                            bannerImage
                            title{
                                userPreferred
                            }
                            coverImage{
                                large
                            }
                        }
                    }
                    ... on TextActivity{
                        id
                        type
                        text
                        replyCount
                        isLocked
                        isSubscribed
                        isLiked
                        isPinned
                        likeCount
                        createdAt
                        user{
                            id
                            name
                            avatar{
                                large
                            }
                        }
                    }
                    ... on MessageActivity{
                        id
                        type
                        message
                        replyCount
                        isPrivate
                        isLocked
                        isSubscribed
                        isLiked
                        likeCount 
                        createdAt
                        user:recipient{
                            id
                        }
                        messenger{
                            id
                            name
                            donatorTier
                            donatorBadge
                            moderatorRoles
                            avatar{
                                large
                            }
                        }
                    }
                }
            }
            }
        """