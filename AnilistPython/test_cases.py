from .__init__ import Anilist
instance = Anilist()

from .deep_search import DeepSearch
ds = DeepSearch()

class TestCase:
    '''
        Simple AnilistPython test case module provided to the users.
    '''
    def __init__(self):
        pass

    # BOT SUPPORT ====================================================================================
    def runTests(self):
        '''
        Test case runner. (Depending on your internet connection, runtime should be ~5 seconds)
        '''
        self.test_getAnime()
        self.test_getAnimeWithID()

        self.test_getCharacter()
        self.test_getCharacterWithID()

        self.test_anilistAnimeInfo()
        self.test_deepSearch()

        self.test_searchAnime()

    def test_getAnime(self):
        data = instance.get_anime("Code Geass Rebellion")
        assert data["name_romaji"] == "Code Geass: Hangyaku no Lelouch"
        assert data["name_english"] == "Code Geass: Lelouch of the Rebellion"
        assert data["starting_time"] == "10/6/2006"
        assert data["ending_time"] == "7/28/2007"
        assert data["airing_episodes"] == 25

    def test_getAnimeDatabase(self):
        pass

    def test_getAnimeWithID(self):
        ID = 13759 #Sakurasou
        data = instance.get_anime_with_id(ID)
        assert data["name_romaji"] == "Sakurasou no Pet na Kanojo"
        assert data["name_english"] == "The Pet Girl of Sakurasou"
        assert data["starting_time"] == "10/9/2012"
        assert data["ending_time"] == "3/26/2013"
        assert data["airing_episodes"] == 24

    def test_getCharacter(self):
        data = instance.get_character("Emilia Tan")
        assert data["first_name"] == "Emilia"
        assert data["last_name"] == None
        assert data["native_name"] == "エミリア"
        assert data["image"] == "https://s4.anilist.co/file/anilistcdn/character/large/b88572-v2KimyNuU4XZ.jpg"

    def test_getCharacterWithID(self):
        ID = 42314 #Harutora from Tokyo Ravens
        data = instance.get_character_with_id(ID)
        assert data["first_name"] == "Harutora"
        assert data["last_name"] == 'Tsuchimikado'
        assert data["native_name"] == "土御門 春虎"
        assert data["image"] == "https://s4.anilist.co/file/anilistcdn/character/large/42314.jpg"

    def test_anilistAnimeInfo(self):
        data = instance.get_anime("Konosuba S1")
        assert data["name_romaji"] == "Kono Subarashii Sekai ni Shukufuku wo! 2"
        assert data["name_english"] == "KONOSUBA -God's blessing on this wonderful world! 2"
        assert data["starting_time"] == "1/12/2017"
        assert data["ending_time"] == "3/16/2017"
        assert data["airing_episodes"] == 10

    def test_deepSearch(self):
        assert ds.deep_search_name_conversion("Code Geass") == 'コードギアス'
        assert ds.deep_search_name_conversion("Eighty-Six") == '86'
        assert ds.deep_search_name_conversion("Re:Zero") == 'Re：ゼロから始める異世界生活'
        assert ds.deep_search_name_conversion("Tensei Slime") == '転生したらスライム'
        assert ds.deep_search_name_conversion("Princess Connect") == 'プリンセスコネクト'

    def test_searchAnime(self):
        data = instance.get_anime('Re:Zero kara Hajimeru Isekai Seikatsu')
        assert instance.search_anime(genre=['Action', 'Adventure', 'Drama', 'Fantasy', 'Psychological', 'Romance', 'Thriller'], year='2016', score=range(80, 90)) == [data]

        data_id = instance.get_anime_id('Re:Zero kara Hajimeru Isekai Seikatsu')
        assert instance.search_anime(genre=['Action', 'Adventure', 'Drama', 'Fantasy', 'Psychological', 'Romance', 'Thriller'], year='2016', score=range(80, 90), id_only=True) == [str(data_id)]
        


testCase = TestCase()
testCase.runTests()
print('=====================================')
print("|  TEST COMPLETED! NO ERRORS FOUND! |")
print('=====================================')
