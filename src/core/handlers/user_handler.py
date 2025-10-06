"""
User business logic handler.
Handles all user-related operations and data processing.
"""
from typing import Dict, Optional
from src.core.search_manager import SearchManager


class UserHandler:
    """
    Handles user business logic operations.
    """
    
    def __init__(self, search_manager: SearchManager):
        """
        Initialize user handler with injected dependencies.
        
        :param search_manager: Manager for handling user search operations
        """
        self.search_manager = search_manager
    
    def get_user_activity(self, page: int, per_page: int) -> Optional[Dict]:
        """
        Get user activity data.
        
        :param page: Page number to retrieve
        :param per_page: Number of items per page
        :return: Dictionary containing user activity data or None if not found
        """
        try:
            activity = self.search_manager.id_search_handler.user_activity(page, per_page)
            
            if not activity or 'data' not in activity:
                return None
            
            activity_data = activity["data"]
            return activity_data if activity_data else None
            
        except Exception:
            return None