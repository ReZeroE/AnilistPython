# MIT License
#
# Copyright (c) 2025 Kevin L.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


"""
Character API module providing user-facing methods for character operations.
Refactored to use dependency injection and business logic separation.
"""
from typing import Dict, Optional, List

try:
    # Try relative imports (when imported as package)
    from ..core.handlers.character_handler import CharacterHandler
    from ..core.search_manager import SearchManager
    from ..core.models.character.character_model import CharacterModel
except ImportError:
    # Fall back to absolute imports (when run directly)
    from src.core.handlers.character_handler import CharacterHandler
    from src.core.search_manager import SearchManager
    from src.core.models.character.character_model import CharacterModel


class Character:
    """
    Main Character API class providing user-facing methods.
    Uses dependency injection to separate business logic from API interface.
    """
    
    def __init__(self, access_info: Dict):
        """
        Initialize Character API with access configuration.
        
        :param access_info: Dictionary containing API access configuration
        """
        __search_manager = SearchManager(access_info)
        self.handler = CharacterHandler(__search_manager)


    def get_character(self, character_name: str, page: int = 1, per_page: int = 5) -> List[CharacterModel]:
        """
        Retrieve character information by name.

        :param character_name: The name of the character to search for
        :param page: The page number to retrieve
        :param per_page: The number of items per page
        :return: List containing character CharacterModel, or empty list if not found
        """
        return self.handler.get_character_by_name(character_name, page, per_page)


    def get_character_by_id(self, character_id: int) -> Optional[CharacterModel]:
        """
        Retrieve character information by ID.

        :param character_id: The character ID number
        :return: CharacterModel object containing parsed character data, or None if not found
        """
        return self.handler.get_character_data_by_id(character_id)
