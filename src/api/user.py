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
User API module providing user-facing methods for user operations.
Refactored to use dependency injection and business logic separation.
"""
from typing import Dict, Optional

try:
    # Try relative imports (when imported as package)
    from ..core.handlers.user_handler import UserHandler
    from ..core.search_manager import SearchManager
except ImportError:
    # Fall back to absolute imports (when run directly)
    from src.core.handlers.user_handler import UserHandler
    from src.core.search_manager import SearchManager


class User:
    """
    Main User API class providing user-facing methods.
    Uses dependency injection to separate business logic from API interface.
    """
    
    def __init__(self, access_info: Dict):
        """
        Initialize User API with access configuration.

        :param access_info: Dictionary containing API access configuration
        """
        __search_manager = SearchManager(access_info)
        self.handler = UserHandler(__search_manager)

    def get_user_activity(self, page: int = 1, per_page: int = 5) -> Optional[Dict]:
        """
        Retrieve user activity data.

        :param page: Page number to retrieve
        :param per_page: Number of items per page
        :return: Dictionary containing user activity data, or None if not found
        """
        return self.handler.get_user_activity(page, per_page)