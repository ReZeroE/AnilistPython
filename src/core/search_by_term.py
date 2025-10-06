"""
ID extraction service for AniList API.
Refactored from retrieve_id.py to follow single responsibility and dependency injection patterns.
"""
import json
import requests
from typing import Dict, Optional
from src.core.queries.query_manager import QueryManager
from src.constants import ERROR_MESSAGES


class SearchByTerm:
    """
    Service class for extracting IDs from AniList API search results.
    """
    
    def __init__(self, access_config: Dict):
        """
        Initialize ID extractor with access configuration.
        
        :param access_config: Dictionary containing API access configuration
        """
        self.access = access_config
        self.query_manager = QueryManager()
    
    def anime(self, term: str, page: int = 1, per_page: int = 3) -> Optional[Dict]:
        """
        Search for anime by string (words).
        
        :param term: Name of the anime to search for
        :param page: Which page to start looking at (default: 1)
        :param per_page: Number of retrieved results from the page (default: 3)
            
        :return: Dictionary containing search results or None if failed
           :return:  
        :return: Raises:
        :return: Exception: If API request fails
        """
        return self._make_search_request(
            query=self.query_manager.anime_queries.anime_query_by_name,
            variables={"query": term, "page": page, "perpage": per_page}
        )
    
    def character(self, term: str, page: int = 1, per_page: int = 3) -> Optional[Dict]:
        """
        Search for character by string (words).
        
            :param term: Name of the character to search for
            :param page: Which page to start looking at (default: 1)
            :param per_page: Number of retrieved results from the page (default: 3)
            
        :return: Dictionary containing search results or None if failed
           :return:  
        :return: Raises:
        :return: Exception: If API request fails
        """
        return self._make_search_request(
            query=self.query_manager.character_queries.character_query_by_name,
            variables={"query": term, "page": page, "perpage": per_page}
        )
    
    def manga(self, term: str, page: int = 1, per_page: int = 3) -> Optional[Dict]:
        """
        Search for manga by string (words).
        
            :param term: Name of the manga to search for
            :param page: Which page to start looking at (default: 1)
            :param per_page: Number of retrieved results from the page (default: 3)
            
        :return: Dictionary containing search results or None if failed
           :return:  
        :return: Raises:
        :return: Exception: If API request fails
        """
        return self._make_search_request(
            query=self.query_manager.manga_queries.manga_query_by_name,
            variables={"query": term, "page": page, "perpage": per_page}
        )
    
    def _make_search_request(self, query: str, variables: Dict) -> Optional[Dict]:
        """
        Make search API request to AniList GraphQL endpoint.
        
            :param query: GraphQL query string
            :param variables: Query variables
            
        :return: Parsed JSON response or None if failed
           :return:  
        :return: Raises:
        :return: Exception: If API request fails
        """
        try:
            response = requests.post(
                self.access['apiurl'],
                headers=self.access['header'],
                json={'query': query, 'variables': variables},
                timeout=30
            )
            
            if response.status_code != 200:
                raise Exception(ERROR_MESSAGES["DATA_POST_UNSUCCESSFUL"].format(response.status_code))
            
            return json.loads(response.text)
            
        except (ValueError, TypeError, requests.RequestException):
            return None