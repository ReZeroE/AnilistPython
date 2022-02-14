import re
from .support_files.translate import AnilistPythonTranslate

class DeepSearch():
    '''
    Translation wrapper module that offers more accurate search/retrieval results Currently in BETA testing phase.
    '''
    def __init__(self):
        pass

    def deep_search_name_conversion(self, anime_name) -> str:
        '''
        Function for converting the name of the anime into Japanese using the built-in Google translator.
        Note: this is an optional function due to its instability (translation failures).

        :param anime_name: the name of the anime to be searched
        :rtype: str
        '''
        translator = AnilistPythonTranslate(source='english', target='japanese')
        anime_name_jp = translator.translate(f'{anime_name} anime')

        # deep search failed
        if re.search('^[a-zA-Z]*$', anime_name_jp) != None:
            return '-1'

        anime_name_final = anime_name_jp.replace(' ', '').replace('アニメ', '')
        
        # print(anime_name_final)
        return anime_name_final



