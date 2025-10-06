"""
Translated search utilities for AnilistPython.
Provides translation-based search functionality for more accurate results.
"""

from .translated_search import TranslatedSearch
from .translate import AnilistPythonTranslate
from .exceptions import TranslationError, InvalidInput, DeepSearchError
from .base_translator import BaseTranslator
from .translate_constants import GOOGLE_LANGUAGES_TO_CODES, GOOGLE_CODES_TO_LANGUAGES

__all__ = [
    'TranslatedSearch',
    'AnilistPythonTranslate', 
    'TranslationError',
    'InvalidInput',
    'DeepSearchError',  # Legacy alias
    'BaseTranslator',
    'GOOGLE_LANGUAGES_TO_CODES',
    'GOOGLE_CODES_TO_LANGUAGES'
]