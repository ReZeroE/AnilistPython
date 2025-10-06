"""
Anime business logic handler.
Handles all anime-related operations and data processing.
"""
from typing import Dict, Optional, Union, List
from datetime import datetime
from src.core.search_manager import SearchManager
from src.core.models.anime.anime_model import AnimeModel

class AnimeHandler:
    """
    Handles anime business logic operations.
    """

    def __init__(self, search_manager: SearchManager):
        """
        Initialize anime handler with injected dependencies.

        :param search_manager: Manager for handling anime search operations
        self.search_manager = search_manager
        """
        self.search_manager = search_manager
    
    def get_anime_by_name(self, anime_name: str, page: int, per_page: int) -> List[AnimeModel]:
        """
        Get anime data by name.

        :param anime_name: Name of the anime
        :param page: Page number
        :param per_page: Items per page
        :return: List of AnimeModel objects
        """
        data = self.search_manager.term_search_handler.anime(anime_name, page, per_page)
        media_list = data['data']['Page']['media']
        
        if not media_list:
            return []
        
        return [AnimeModel(media) for media in media_list]
    
    def get_anime_data_by_id(self, anime_id: int|str) -> Optional[AnimeModel]:
        """
        Get anime data by ID.

        :param anime_id: The anime ID
        :return: AnimeModel object or None if not found
        """
        if isinstance(anime_id, int):
            anime_id = str(anime_id)
            
        try:
            data = self.search_manager.id_search_handler.anime(anime_id)
            media_data = data['data']['Media']
            return AnimeModel(media_data)
        except Exception as ex:
            print(ex)
            return None

    