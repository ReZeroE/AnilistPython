import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from src import Anilist, CharacterModel
from .utils import rate_limit_delay


class TestCharacterIntegration:
    
    @pytest.fixture
    def anilist(self) -> Anilist:
        return Anilist()
    
    def test_character_integration(self, anilist: Anilist):
        rate_limit_delay()
        
        # fetch character by name
        search_results = anilist.character.get_character("Edward", 1, 3)
        assert search_results is not None
        assert isinstance(search_results, list)
        assert len(search_results) > 0
        assert all(isinstance(character, CharacterModel) for character in search_results)

        # fetch character by id
        character_id = search_results[0].id
        search_result_by_id = anilist.character.get_character_by_id(character_id)
        assert search_result_by_id is not None
        assert isinstance(search_result_by_id, CharacterModel)
        assert search_result_by_id.name == search_results[0].name
        
        
    def test_character_integration_to_dict(self, anilist: Anilist):
        rate_limit_delay()
        
        # fetch character by name
        search_results = anilist.character.get_character("Asuka", 1, 3)
        assert search_results is not None
        assert isinstance(search_results, list)
        assert len(search_results) > 0
        assert all(isinstance(character, CharacterModel) for character in search_results)

        character_dict = search_results[0].to_dict()
        assert isinstance(character_dict, dict)
        assert character_dict['id'] == search_results[0].id
        assert character_dict['name'] == search_results[0].name
        assert character_dict['name_native'] == search_results[0].name_native
        assert character_dict['description'] == search_results[0].description
        assert character_dict['image'] == search_results[0].image