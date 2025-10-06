"""
Manga business logic handler.
Handles all manga-related operations and data processing.
"""
from typing import Dict, Optional, Union, List
from src.core.search_manager import SearchManager
from src.core.models.manga.manga_model import MangaModel


class MangaHandler:
    """
    Handles manga business logic operations.
    """
    
    def __init__(self, search_manager: SearchManager):
        """
        Initialize manga handler with injected dependencies.
        
        :param search_manager: Manager for handling manga search operations
        """
        self.search_manager = search_manager
    
    def get_manga_by_name(self, manga_name: str, page: int, per_page: int) -> List[MangaModel]:
        """
        Get manga data by name.
        
        :param manga_name: Name of the manga
        :param page: Page number
        :param per_page: Items per page
        :return: List of MangaModel objects
        """
        data = self.search_manager.term_search_handler.manga(manga_name, page, per_page)
        media_list = data['data']['Page']['media']
        
        if not media_list:
            return []
        
        return [MangaModel(manga) for manga in media_list]
    
    def get_data_by_id(self, manga_id: int|str) -> Optional[MangaModel]:
        """
        Get manga data by ID.
        
        :param manga_id: The manga ID
        :return: MangaModel object or None if not found
        """
        if isinstance(manga_id, int):
            manga_id = str(manga_id)

        try:
            data = self.search_manager.id_search_handler.manga(manga_id)
            manga_data = data['data']['Media']
            return MangaModel(manga_data)
        except Exception:
            return None