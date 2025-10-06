import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from src import Anilist, MangaModel
from .utils import rate_limit_delay


class TestMangaIntegration:
    
    @pytest.fixture
    def anilist(self) -> Anilist:
        return Anilist()
    
    def test_manga_integration(self, anilist: Anilist):
        rate_limit_delay()
        
        # fetch manga by name
        search_results = anilist.manga.get_manga("Death Note", 1, 3)
        assert search_results is not None
        assert isinstance(search_results, list)
        assert len(search_results) > 0
        assert all(isinstance(manga, MangaModel) for manga in search_results)

        # fetch manga by id
        manga_id = search_results[0].id
        search_result_by_id = anilist.manga.get_manga_by_id(manga_id)
        assert search_result_by_id is not None
        assert isinstance(search_result_by_id, MangaModel)
        assert search_result_by_id.title_romaji == search_results[0].title_romaji
        
        
    def test_manga_integration_to_dict(self, anilist: Anilist):
        rate_limit_delay()
        
        # fetch manga by name
        search_results = anilist.manga.get_manga("One Piece", 1, 3)
        assert search_results is not None
        assert isinstance(search_results, list)
        assert len(search_results) > 0
        assert all(isinstance(manga, MangaModel) for manga in search_results)

        manga_dict = search_results[0].to_dict()
        assert isinstance(manga_dict, dict)
        assert manga_dict['id'] == search_results[0].id
        assert manga_dict['title'] == search_results[0].title
        assert manga_dict['cover_image'] == search_results[0].cover_image
        assert manga_dict['tags'] == search_results[0].tags
        assert manga_dict['banner_image'] == search_results[0].banner_image
        assert manga_dict['format'] == search_results[0].format
        assert manga_dict['chapters'] == search_results[0].chapters
        assert manga_dict['volumes'] == search_results[0].volumes
        assert manga_dict['status'] == search_results[0].status
        assert manga_dict['description'] == search_results[0].description
        assert manga_dict['average_score'] == search_results[0].average_score
        assert manga_dict['mean_score'] == search_results[0].mean_score
        assert manga_dict['genres'] == search_results[0].genres
        assert manga_dict['synonyms'] == search_results[0].synonyms
        assert manga_dict['season'] == search_results[0].season
        assert manga_dict['hashtag'] == search_results[0].hashtag
        assert manga_dict['is_adult'] == search_results[0].is_adult