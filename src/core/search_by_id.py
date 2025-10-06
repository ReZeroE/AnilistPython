"""
Data extraction service for AniList API.
Refactored from retrieve_data.py to follow single responsibility and dependency injection patterns.
"""
import os
import datetime
import json
import requests
from typing import Dict, Optional
from src.core.queries.query_manager import QueryManager
from src.constants import ERROR_MESSAGES


class SearchById:
    """
    Service class for extracting data from AniList API.
    """
    
    def __init__(self, access_config: Dict):
        """
        Initialize data extractor with access configuration.
        
        :param access_config: Dictionary containing API access configuration
        :param status: Boolean status for bot support
        """
        self.access = access_config
        self.query_manager = QueryManager()
        self.logfile = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'error-log.txt')
    
    def anime(self, anime_id: str) -> Optional[Dict]:
        """
        Extract anime information by ID.
        
        :param anime_id: The anime ID number
            
        :return: Dictionary containing anime data or None if failed
           :return:  
        :return: Raises:
        :return: Exception: If function status is False or API request fails
        """
        return self._make_api_request(
            query=self.query_manager.anime_queries.anime_query_by_id,
            variables={
                "id": anime_id
            }
        )
    
    def manga(self, manga_id: str) -> Optional[Dict]:
        """
        Extract manga information by ID.
        
            :param manga_id: The manga ID number
            
        :return: Dictionary containing manga data or None if failed
           :return:  
        :return: Raises:
        :return: Exception: If function status is False or API request fails
        """
        return self._make_api_request(
            query=self.query_manager.manga_queries.manga_query_by_id,
            variables={
                "id": manga_id
            }
        )
    
    def character(self, character_id: str) -> Optional[Dict]:
        """
        Extract character information by ID.
        
            :param character_id: The character ID number
            
        :return: Dictionary containing character data or None if failed
           :return:  
        :return: Raises:
        :return: Exception: If function status is False or API request fails
        """
        return self._make_api_request(
            query=self.query_manager.character_queries.character_query_by_id,
            variables={
                "id": character_id
            }
        )
    
    def staff(self, staff_id: str) -> Optional[Dict]:
        """
        Extract staff information by ID.
        
            :param staff_id: The staff ID number
            
        :return: Dictionary containing staff data or None if failed
           :return:  
        :return: Raises:
        :return: Exception: If function status is False or API request fails
        """
        return self._make_api_request(
            query=self.query_manager.staff_queries.staff_query_by_id,
            variables={
                "id": staff_id
            }
        )
    
    def user_activity(self, page: int, per_page: int) -> Optional[Dict]:
        """
        Extract user activity data.
        
            :param page: Page number
            :param per_page: Items per page
            
        :return: Dictionary containing user activity data or None if failed
           :return:  
        :return: Raises:
        :return: Exception: If function status is False or API request fails
        """
        return self._make_api_request(
            query=self.query_manager.user_queries.user_query,
            variables={
                "page": page, 
                "perPage": per_page
            }
        )
    
    def _make_api_request(self, query: str, variables: Dict) -> Optional[Dict]:
        """
        Make API request to AniList GraphQL endpoint.
        
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
                json={
                    'query': query, 
                    'variables': variables
                },
                timeout=30
            )
            
            if response.status_code != 200:
                raise Exception(ERROR_MESSAGES["DATA_POST_UNSUCCESSFUL"].format(response.status_code))
            
            return json.loads(response.text)
            
        except (ValueError, TypeError, requests.RequestException):
            self._log_error(f"API request failed: {query[:50]}...")
            return None
    
    def _log_error(self, error_message: str) -> None:
        """
        Log error to file with timestamp.
        
            :param error_message: Error message to log
        """
        try:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(self.logfile, 'a', encoding='utf-8') as f:
                f.write(f"[{timestamp}] {error_message}\n")
        except IOError:
            pass  # Silently fail if logging fails