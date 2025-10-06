import json
from datetime import datetime


class AnimeModel:
    """
    Anime data model representing an anime.
    Provides structured access to anime attributes.
        
    Use `.to_dict()` to convert to a Python dictionary.
    """
    def __init__(self, data: dict):
        self.id: int = None
        self.title: str = None
        self.title_romaji: str = None
        self.start_date: datetime = None
        self.end_date: datetime = None
        self.cover_image: str = None
        self.banner_image: str = None
        self.format: str = None
        self.status: str = None
        self.episodes: int = None
        self.season: str = None
        self.description: str = None
        self.average_score: int = None
        self.mean_score: int = None
        self.genres: list = []
        self.synonyms: list = []
        self.next_airing_episode: AnimeNextAiringEpModel = None
        
        # populate model attributes from data dictionary
        self.to_model(data)

    def __str__(self):
        return json.dumps(self.to_dict(), indent=4, default=self.__datetime_serializer)

    def __hash__(self):
        return hash(self.to_dict())


    def to_model(self, data: dict):
        """
        Parse the data dictionary and populate model attributes.
        """
        self.id = data.get('id')
        title_data = data.get('title')
        if title_data:
            self.title_romaji = title_data.get('romaji')
            self.title_english = title_data.get('english')
            # default english title to romaji if not available
            if self.title_english == None:
                self.title_english = self.title_romaji

        start_date_data = data.get('startDate')
        end_date_data = data.get('endDate')
        self.start_date = self.__format_datetime(start_date_data)
        self.end_date = self.__format_datetime(end_date_data)
        
        cover_image_data: dict = data.get('coverImage')
        if cover_image_data:
            self.cover_image = cover_image_data.get('large')
        
        next_airing_data = data.get('nextAiringEpisode')
        if next_airing_data:
            self.next_airing_episode = AnimeNextAiringEpModel()
            self.next_airing_episode.to_model(next_airing_data)
        
        self.banner_image = data.get('bannerImage')
        self.format = data.get('format')
        self.status = data.get('status')
        self.episodes = data.get('episodes')
        self.season = data.get('season')
        self.description = data.get('description')
        self.average_score = data.get('averageScore')
        self.mean_score = data.get('meanScore')
        self.genres = data.get('genres', [])
        self.synonyms = data.get('synonyms', [])
    
    
    def to_dict(self) -> dict:
        """
        Convert the AnimeModel to a Python dictionary.
        """
        return {
            "id": self.id,
            "title": self.title,
            "title_romaji": self.title_romaji,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "cover_image": self.cover_image,
            "banner_image": self.banner_image,
            "format": self.format,
            "status": self.status,
            "episodes": self.episodes,
            "season": self.season,
            "description": self.description,
            "average_score": self.average_score,
            "mean_score": self.mean_score,
            "genres": self.genres,
            "synonyms": self.synonyms,
            "next_airing_episode": self.next_airing_episode.to_dict() if self.next_airing_episode else None
        }


    def __format_datetime(self, date_data: dict) -> datetime:
        if not date_data or not all(date_data.get(key) for key in ['year', 'month', 'day']):
            return None
        
        try:
            return datetime(
                date_data['year'],
                date_data['month'],
                date_data['day']
            )
        except (ValueError, TypeError):
            return None
        
    def __datetime_serializer(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        raise TypeError(f"Object of type {type(obj)} is not JSON serializable")


class AnimeNextAiringEpModel:
    def __init__(self, data: dict = None):
        self.airing_at: int = None
        self.time_until_airing: int = None
        self.episode: int = None
        
        if data:
            self.to_model(data)
    
    def to_model(self, data: dict):
        self.airing_at = data.get('airingAt')
        self.time_until_airing = data.get('timeUntilAiring')
        self.episode = data.get('episode')
    
    def to_dict(self) -> dict:
        return {
            "airing_at": self.airing_at,
            "time_until_airing": self.time_until_airing,
            "episode": self.episode
        }