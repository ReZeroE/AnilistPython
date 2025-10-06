import json
from datetime import datetime


class CharacterModel:
    """
    Character data model representing a character.
    Provides structured access to character attributes.
        
    Use `.to_dict()` to convert to a Python dictionary.
    """
    def __init__(self, data: dict):
        self.id: int = None
        self.name: str = None
        self.name_native: str = None
        self.description: str = None
        self.image: str = None
        
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
        
        name_data = data.get('name')
        if name_data:
            # Combine first and last name for the name field
            first_name = name_data.get('first') or ''
            last_name = name_data.get('last') or ''
            
            # Create full name, handling None and empty strings
            if first_name and last_name:
                self.name = f"{first_name} {last_name}".strip()
            elif first_name:
                self.name = first_name.strip()
            elif last_name:
                self.name = last_name.strip()
            else:
                self.name = None
                
            self.name_native = name_data.get('native')
            
            # if name is not available, set name as name_native
            if not self.name and self.name_native:
                self.name = self.name_native
        
        self.description = data.get('description')
        
        image_data: dict = data.get('image')
        if image_data:
            self.image = image_data.get('large')
    
    
    def to_dict(self) -> dict:
        """
        Convert the CharacterModel to a Python dictionary.
        """
        return {
            "id": self.id,
            "name": self.name,
            "name_native": self.name_native,
            "description": self.description,
            "image": self.image
        }


    def __datetime_serializer(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        raise TypeError(f"Object of type {type(obj)} is not JSON serializable")