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
Manga API module providing user-facing methods for manga operations.
Refactored to use dependency injection and business logic separation.
"""
from typing import Dict, Optional, List

try:
    # Try relative imports (when imported as package)
    from ..core.handlers.manga_handler import MangaHandler
    from ..core.search_manager import SearchManager
    from ..core.models.manga.manga_model import MangaModel
except ImportError:
    # Fall back to absolute imports (when run directly)
    from src.core.handlers.manga_handler import MangaHandler
    from src.core.search_manager import SearchManager
    from src.core.models.manga.manga_model import MangaModel


class Manga:
    """
    Main Manga API class providing user-facing methods.
    Uses dependency injection to separate business logic from API interface.
    """
    
    def __init__(self, access_info: Dict):
        """
        Initialize Manga API with access configuration.
        
        :param access_info: Dictionary containing API access configuration
        """
        __search_manager = SearchManager(access_info)
        self.handler = MangaHandler(__search_manager)


    def get_manga(self, manga_name: str, page: int = 1, per_page: int = 5) -> List[MangaModel]:
        """
        Retrieve manga information by name.

        :param manga_name: The name of the manga to search for
        :param page: The page number to retrieve
        :param per_page: The number of items per page
        :return: List containing manga MangaModel, or empty list if not found
        """
        return self.handler.get_manga_by_name(manga_name, page, per_page)

    def get_manga_by_id(self, manga_id: int|str) -> Optional[MangaModel]:
        """
        Retrieve manga information by ID.

        :param manga_id: The manga ID number
        :return: MangaModel object containing parsed manga data, or None if not found
        """
        return self.handler.get_data_by_id(manga_id)