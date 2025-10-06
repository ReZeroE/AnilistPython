try:
    from .search_by_id import SearchById
    from .search_by_term import SearchByTerm
except ImportError:
    from src.core.search_by_id import SearchById
    from src.core.search_by_term import SearchByTerm

class SearchManager:
    def __init__(self, access_config: dict):
        self.term_search_handler = SearchByTerm(access_config)
        self.id_search_handler = SearchById(access_config)
        
    