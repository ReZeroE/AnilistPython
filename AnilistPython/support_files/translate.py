from .constants import BASE_URLS, GOOGLE_LANGUAGES_TO_CODES
from .deep_search_exceptions import DeepSearchError, InvalidInput
from .translate_structure import BaseTranslator

from time import sleep
import requests
import re

class AnilistPythonTranslate(BaseTranslator):
    """
    class that wraps functions, which use google translate under the hood to translate text(s)
    """
    _languages = GOOGLE_LANGUAGES_TO_CODES
    supported_languages = list(_languages.keys())

    def __init__(self, source="en", target="ja", proxies=None, **kwargs):
        """
        @param source: source language to translate from
        @param target: target language to translate to
        """
        self.__base_url = BASE_URLS.get("GOOGLE_TRANSLATE")
        self.proxies = proxies

        self._source, self._target = self.map_language_to_code(source.lower(), target.lower())

        super(AnilistPythonTranslate, self).__init__(base_url=self.__base_url,
                                               source=self._source,
                                               target=self._target,
                                               element_tag='div',
                                               payload_key='q',  # key of text in the url
                                               hl=self._target,
                                               sl=self._source,
                                               **kwargs)

    def map_language_to_code(self, *languages):
        """
        map language to its corresponding code (abbreviation) if the language was passed by its full name by the user
        @param languages: list of languages
        @return: mapped value of the language or raise an exception if the language is not supported
        """
        for language in languages:
            if language in self._languages.values() or language == 'auto':
                yield language
            elif language in self._languages.keys():
                yield self._languages[language]
            else:
                raise InvalidInput(language)


    def translate(self, text, **kwargs):
        """
        function that uses google translate to translate a text
        @param text: desired text to translate
        @return: str: translated text
        """
        if self._validate_payload(text):
            text = text.strip()

            if self.payload_key:
                self._url_params[self.payload_key] = text

            response = requests.get(self.__base_url,
                                    params=self._url_params)
                                    
            if response.status_code == 429:
                raise InvalidInput(response.status_code)

            if response.status_code != 200:
                raise InvalidInput(response.status_code)

            translated_text = re.search('<div class="result-container">.*?</div>', response.text).group(0)
            translated_text = translated_text.replace('<div class="result-container">', '').replace('</div>', '')
            return translated_text




