class QSData:
    '''
    Class for storing query strings.
    '''
    def __init__(self):
        # ANIME =====================================================
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

        # MANGA =====================================================
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

        # STAFF =====================================================
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

        # STUDIO =====================================================
        self.studioInfoQS = """\
            query ($id: Int) {
                Studio(id: $id) {
                    name
                }
            }
        """

        # CHARACTER =====================================================
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

        # REVIEW =====================================================
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


        # ANIME ID ===================================================================
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

        # CHARACTER ID ===================================================================
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

        # MANGA ID ===================================================================
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

        # STAFF ID ===================================================================
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

        # STUDIO ID ===================================================================
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

        # GET AUTHENTICATED CURRENT USER ID
        self.user_get_idQS = """\
            query{
	            Viewer{
		            id
	            }
            }
        """

        # GET AUTHENTICATED CURRENT ACTIVITY
        self.user_activyQS = """\
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