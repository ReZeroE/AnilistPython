"""
Unified query strings accessor for backward compatibility.
"""
from .anime_queries import AnimeQueries
from .manga_queries import MangaQueries
from .character_queries import CharacterQueries
from .user_queries import UserQueries
from .staff_studio_queries import StaffQueries, StudioQueries
from .review_queries import ReviewQueries


class QueryManager:
    """
    Unified query strings class for backward compatibility.
    This class aggregates all query types into a single interface.
    """
    def __init__(self):
        # Initialize all query classes
        self.anime_queries = AnimeQueries()
        self.manga_queries = MangaQueries()
        self.character_queries = CharacterQueries()
        self.user_queries = UserQueries()
        self.staff_queries = StaffQueries()
        self.studio_queries = StudioQueries()
        self.review_queries = ReviewQueries()
