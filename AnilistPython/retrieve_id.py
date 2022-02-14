import json
import requests
from .query_strings import QSData
qsObj = QSData()

class ExtractID:
    def __init__(self, access, status):
        self.access = access
        self.status = status # Boolean value used for bots

    def anime(self, term, page = 1, perpage = 3):
        """
        Search for anime by string (words)
        Page shows which page the result is currently on.
        Perpage represents the number of items retrieved.
        
        :param term str: Name of the anime
        :param page int: Which page for the program to start looking at. Default = 1
        :param perpage int: Number of retreived results from the page
        :return: A list of perpage num elements containing the dictionaries of each anime or None.
        :rtype: dict list or None
        """

        preset = {"query": term, "page": page, "perpage": perpage}
        req = requests.post(self.access['apiurl'],
                          headers=self.access['header'],
                          json={'query': qsObj.animeIDQS, 'variables': preset})

        if req.status_code != 200:
            raise Exception(f"Data post unsuccessful. ({req.status_code})")

        try:
            extracted_data = json.loads(req.text)
        except ValueError:
            return None
        except TypeError:
            return None
        else:
            return extracted_data


    def character(self, term, page = 1, perpage = 3):
        """
        Search for a character by string (words).
        Page shows which page the result is currently on.
        Perpage represents the number of items retrieved.
        
        :param term str: Name of the character
        :param page int: Which page for the program to start looking at. Default = 1
        :param perpage int: Number of retreived results from the page
        :return: A list of perpage num elements containing the dictionaries of each character or None.
        :rtype: dict list or None
        """

        preset = {"query": term, "page": page, "perpage": perpage}
        req = requests.post(self.access['apiurl'],
                          headers=self.access['header'],
                          json={'query': qsObj.characterIDQS, 'variables': preset})

        if req.status_code != 200:
            raise Exception(f"Data post unsuccessful. ({req.status_code})")

        try:
            extracted_data = json.loads(req.text)
        except ValueError:
            return None
        except TypeError:
            return None
        else:
            return extracted_data
                    
    def manga(self, term, page = 1, perpage = 3):
        """
        Search for a Manga by string (words).
        Page shows which page the result is currently on.
        Perpage represents the number of items retrieved.
        
        :param term str: Name of the Manga
        :param page int: Which page for the program to start looking at. Default = 1
        :param perpage int: Number of retreived results from the page
        :return: A list of perpage num elements containing the dictionaries of each Manga or None.
        :rtype: dict list or None
        """

        preset = {"query": term, "page": page, "perpage": perpage}
        req = requests.post(self.access['apiurl'],
                          headers=self.access['header'],
                          json={'query': qsObj.mangaIDQS, 'variables': preset})

        if req.status_code != 200:
            raise Exception(f"Data post unsuccessful. ({req.status_code})")

        try:
            extracted_data = json.loads(req.text)
        except ValueError:
            return None
        except TypeError:
            return None
        else:
            return extracted_data
                    
    def staff(self, term, page = 1, perpage = 3):
        """
        Search for a staff by string (words).
        Page shows which page the result is currently on.
        Perpage represents the number of items retrieved.
        
        :param term str: Name of the staff
        :param page int: Which page for the program to start looking at. Default = 1
        :param perpage int: Number of retreived results from the page
        :return: A list of perpage num elements containing the dictionaries of each staff or None.
        :rtype: dict list or None
        """

        preset = {"query": term, "page": page, "perpage": perpage}
        req = requests.post(self.access['apiurl'],
                          headers=self.access['header'],
                          json={'query': qsObj.staffIDQS, 'variables': preset})

        if req.status_code != 200:
            raise Exception(f"Data post unsuccessful. ({req.status_code})")

        try:
            extracted_data = json.loads(req.text)
        except ValueError:
            return None
        except TypeError:
            return None
        else:
            return extracted_data
                    
    def studio(self, term, page = 1, perpage = 3):
        """
        Search for a studio by string (words).
        Page shows which page the result is currently on.
        Perpage represents the number of items retrieved.
        
        :param term str: Name of the studio
        :param page int: Which page for the program to start looking at. Default = 1
        :param perpage int: Number of retreived results from the page
        :return: A list of perpage num elements containing the dictionaries of each studio or None.
        :rtype: dict list or None
        """

        preset = {"query": term, "page": page, "perpage": perpage}
        req = requests.post(self.access['apiurl'],
                          headers=self.access['header'],
                          json={'query': qsObj.studioIDQS, 'variables': preset})

        if req.status_code != 200:
            raise Exception(f"Data post unsuccessful. ({req.status_code})")

        try:
            extracted_data = json.loads(req.text)
        except ValueError:
            return None
        except TypeError:
            return None
        else:
            return extracted_data