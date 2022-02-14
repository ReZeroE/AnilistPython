import os
import datetime
import json
import requests
from .query_strings import QSData
qsObj = QSData()

class ExtractInfo:
    def __init__(self, access, status):
        self.access = access
        self.status = status # Boolean value used for bots

        self.logfile = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'error-log.txt')

    def anime(self, anime_id):
        """
        Function to extract anime info provided the anime ID num.
        Returns None if activte status is False.

        :param anime_id: input anime ID number
        :return: dict or None
        :rtype: dict or NoneType
        """

        if self.status == False:
            raise Exception("Current function status is False.")

        id_val = {"id": anime_id}
        req = requests.post(self.access['apiurl'],
                         headers=self.access['header'],
                         json={'query': qsObj.animeInfoQS, 'variables': id_val})
        
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

    def manga(self, manga_id):
        """
        The function to retrieve an manga's information.
        Returns None if activte status is False.

        :param int manga_id: the manga's ID
        :return: dict or None
        :rtype: dict or NoneType
        """

        if self.status == False:
            raise Exception("Current function status is False.")

        id_val = {"id": manga_id}
        req = requests.post(self.access['apiurl'],
                         headers=self.access['header'],
                         json={'query': qsObj.mangaInfoQS, 'variables': id_val})
        
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

    def staff(self, staff_id):
        """
        The function to retrieve a staff's information.
        Returns None if activte status is False.

        :param int staff_id: the anime's ID
        :return: dict or None
        :rtype: dict or NoneType
        """

        if self.status == False:
            raise Exception("Current function status is False.")

        id_val = {"id": staff_id}
        req = requests.post(self.access['apiurl'],
                         headers=self.access['header'],
                         json={'query': qsObj.staffInfoQS, 'variables': id_val})
        
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

    def studio(self, studio_id):
        """
        The function to retrieve a studio's information.
        Returns None if activte status is False.

        :param int studio_id: the studio's ID
        :return: dict or None
        :rtype: dict or NoneType
        """

        if self.status == False:
            raise Exception("Current function status is False.")

        id_val = {"id": studio_id}
        req = requests.post(self.access['apiurl'],
                         headers=self.access['header'],
                         json={'query': qsObj.studioInfoQS, 'variables': id_val})
        
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

    def character(self, character_id):
        """
        The function to retrieve a character's information.
        Returns None if activte status is False.

        :param int character_id: the character's ID
        :return: dict or None
        :rtype: dict or NoneType
        """

        if self.status == False:
            raise Exception("Current function status is False.")

        id_val = {"id": character_id}
        req = requests.post(self.access['apiurl'],
                         headers=self.access['header'],
                         json={'query': qsObj.characterInfoQS, 'variables': id_val})
        
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

    def review(self, review_id, html):
        """
        Function that retrieve review information. HTML may be set to True of False.
        Returns None if activte status is False.

        :param review_id: the ID of the review
        :param html: boolean to the format of the return value
        :return: json obj -> review info
        :rtype: json obj -> review info
        """

        id_val = {"id": review_id, "html": html}
        req = requests.post(self.access['apiurl'],
                          headers=self.access['header'],
                          json={'query': qsObj.reviewInfoQS, 'variables': id_val})

        try:
            extracted_data = json.loads(req.text)
        except ValueError:
            return None
        except TypeError:
            return None
        else:
            return extracted_data