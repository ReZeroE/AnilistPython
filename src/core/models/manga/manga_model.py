import json
from datetime import datetime


class MangaModel:
    """
    Manga data model representing a manga.
    Provides structured access to manga attributes.
        
    Use `.to_dict()` to convert to a Python dictionary.
    """
    def __init__(self, data: dict):
        self.id: int = None
        self.title: str = None
        self.title_romaji: str = None
        self.start_date: datetime = None
        self.end_date: datetime = None
        self.cover_image: str = None
        self.tags: list = []
        self.banner_image: str = None
        self.format: str = None
        self.chapters: int = None
        self.volumes: int = None
        self.status: str = None
        self.description: str = None
        self.average_score: int = None
        self.mean_score: int = None
        self.genres: list = []
        self.synonyms: list = []
        self.season: str = None
        self.hashtag: str = None
        self.is_adult: bool = None
        
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
        
        # flatten tags structure and access the name field to get the string
        tags_data = data.get('tags', [])
        if tags_data:
            self.tags = [tag.get('name') for tag in tags_data if tag.get('name')]
        
        self.banner_image = data.get('bannerImage')
        self.format = data.get('format')
        self.chapters = data.get('chapters')
        self.volumes = data.get('volumes')
        self.status = data.get('status')
        self.description = data.get('description')
        self.average_score = data.get('averageScore')
        self.mean_score = data.get('meanScore')
        self.genres = data.get('genres', [])
        self.synonyms = data.get('synonyms', [])
        self.season = data.get('season')
        self.hashtag = data.get('hashtag')
        self.is_adult = data.get('isAdult')
    
    
    def to_dict(self) -> dict:
        """
        Convert the MangaModel to a Python dictionary.
        """
        return {
            "id": self.id,
            "title": self.title.to_dict() if self.title else None,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "cover_image": self.cover_image,
            "tags": self.tags,
            "banner_image": self.banner_image,
            "format": self.format,
            "chapters": self.chapters,
            "volumes": self.volumes,
            "status": self.status,
            "description": self.description,
            "average_score": self.average_score,
            "mean_score": self.mean_score,
            "genres": self.genres,
            "synonyms": self.synonyms,
            "season": self.season,
            "hashtag": self.hashtag,
            "is_adult": self.is_adult
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