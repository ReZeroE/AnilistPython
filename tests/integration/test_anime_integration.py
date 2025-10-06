import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from src import Anilist, AnimeModel
from .utils import rate_limit_delay


class TestAnimeIntegration:
    
    @pytest.fixture
    def anilist(self) -> Anilist:
        return Anilist()
    
    def test_anime_integration(self, anilist: Anilist):
        rate_limit_delay()
        
        # fetch anime by name
        search_results = anilist.anime.get_anime("Eighty Six", 1, 3)
        assert search_results is not None
        assert isinstance(search_results, list)
        assert len(search_results) > 0
        assert all(isinstance(anime, AnimeModel) for anime in search_results)

        # fetch anime by id
        anime_id = search_results[0].id
        search_result_by_id = anilist.anime.get_anime_by_id(anime_id)
        assert search_result_by_id is not None
        assert isinstance(search_result_by_id, AnimeModel)
        assert search_result_by_id.title_romaji == search_results[0].title_romaji
        
        
    def test_anime_integration_to_dict(self, anilist: Anilist):
        rate_limit_delay()
        
        # fetch anime by name
        search_results = anilist.anime.get_anime("Magica Madoka", 1, 3)
        assert search_results is not None
        assert isinstance(search_results, list)
        assert len(search_results) > 0
        assert all(isinstance(anime, AnimeModel) for anime in search_results)

        anime_dict = search_results[0].to_dict()
        assert isinstance(anime_dict, dict)
        assert anime_dict['id'] == search_results[0].id
        assert anime_dict['title_romaji'] == search_results[0].title_romaji
        assert anime_dict['title'] == search_results[0].title
        assert anime_dict['cover_image'] == search_results[0].cover_image
        assert anime_dict['banner_image'] == search_results[0].banner_image
        assert anime_dict['format'] == search_results[0].format
        assert anime_dict['status'] == search_results[0].status
        assert anime_dict['episodes'] == search_results[0].episodes
        assert anime_dict['season'] == search_results[0].season
        assert anime_dict['description'] == search_results[0].description
        assert anime_dict['average_score'] == search_results[0].average_score
        assert anime_dict['mean_score'] == search_results[0].mean_score
        assert anime_dict['genres'] == search_results[0].genres
        assert anime_dict['synonyms'] == search_results[0].synonyms
        assert anime_dict['next_airing_episode'] == (search_results[0].next_airing_episode.to_dict() if search_results[0].next_airing_episode else None)
        