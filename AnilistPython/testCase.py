from .botSupport import botSupportClass
anilistBot = botSupportClass()

from .__init__ import Anilist
instance = Anilist()

class TestCase:
    '''
        Test Cases for the botSupport Class
    '''
    def __init__(self):
        pass

    # BOT SUPPORT ====================================================================================
    def runTests(self):
        self.test_botAnimeID()
        self.test_botAnimeInfo()
        self.test_botCharacterID()
        self.test_botCharacterInfo()

    def test_botAnimeInfo(self):
        data = anilistBot.getAnimeInfo("Code Geass Rebellion")
        assert data["name_romaji"] == "Code Geass: Hangyaku no Lelouch"
        assert data["name_english"] == "Code Geass: Lelouch of the Rebellion"
        assert data["starting_time"] == "10/6/2006"
        assert data["ending_time"] == "7/28/2007"
        assert data["airing_episodes"] == 25

    def test_botAnimeID(self):
        ID = 13759 #Sakurasou
        data = anilistBot.getAnimeInfoWithID(ID)
        assert data["name_romaji"] == "Sakurasou no Pet na Kanojo"
        assert data["name_english"] == "The Pet Girl of Sakurasou"
        assert data["starting_time"] == "10/9/2012"
        assert data["ending_time"] == "3/26/2013"
        assert data["airing_episodes"] == 24

    def test_botCharacterInfo(self):
        data = anilistBot.getCharacterInfo("Emilia Tan")
        assert data["first_name"] == "Emilia"
        assert data["last_name"] == None
        assert data["native_name"] == "エミリア"
        assert data["image"] == "https://s4.anilist.co/file/anilistcdn/character/large/b88572-v2KimyNuU4XZ.jpg"

    def test_botCharacterID(self):
        ID = 42314 #Harutora from Tokyo Ravens
        data = anilistBot.getCharacterInfoWithID(ID)
        assert data["first_name"] == "Harutora"
        assert data["last_name"] == 'Tsuchimikado'
        assert data["native_name"] == "土御門 春虎"
        assert data["image"] == "https://s4.anilist.co/file/anilistcdn/character/large/42314.jpg"

    # ANILIST =============================================================================================================
    def test_anilistAnimeInfo(self):
        data = instance.getANimeInfo("Konosuba S1")
        assert data["name_romaji"] == "Kono Subarashii Sekai ni Shukufuku wo! 2"
        assert data["name_english"] == "KONOSUBA -God's blessing on this wonderful world! 2"
        assert data["starting_time"] == "1/12/2017"
        assert data["ending_time"] == "3/16/2017"
        assert data["airing_episodes"] == 10

testCase = TestCase()
testCase.runTests()
print('=====================================')
print("|  TEST COMPLETED! NO ERRORS FOUND! |")
print('=====================================')
