"""
Character business logic handler.
Handles all character-related operations and data processing.
"""
from typing import Dict, Optional, Union, List
from src.core.search_manager import SearchManager
from src.core.models.character.character_model import CharacterModel


class CharacterHandler:
    """
    Handles character business logic operations.
    """
    
    def __init__(self, search_manager: SearchManager):
        """
        Initialize character handler with injected dependencies.
        
        :param search_manager: Manager for handling character search operations
        """
        self.search_manager = search_manager
    
    def get_character_by_name(self, character_name: str, page: int, per_page: int) -> List[CharacterModel]:
        """
        Get character data by name.
        
        :param character_name: Name of the character
        :param page: Page number
        :param per_page: Items per page
        :return: List of CharacterModel objects
        """
        data = self.search_manager.term_search_handler.character(character_name, page, per_page)
        character_list = data['data']['Page']['characters']
        
        if not character_list:
            return []
        
        return [CharacterModel(character_data) for character_data in character_list]
    
    def get_character_data_by_id(self, character_id: int|str) -> Optional[CharacterModel]:
        """
        Get character data by ID.
        
        :param character_id: The character ID
        :return: CharacterModel object or None if not found
        """
        if isinstance(character_id, int):
            character_id = str(character_id)

        try:
            data = self.search_manager.id_search_handler.character(character_id)
            character_data = data['data']['Character']
            return CharacterModel(character_data)
        except Exception:
            return None
