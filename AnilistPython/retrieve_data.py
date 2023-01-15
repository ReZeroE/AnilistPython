# SPDX-License-Identifier: MIT
# MIT License
#
# Copyright (c) 2021 Kevin L.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import json
import requests

from .constants import *

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
                         json={'query': ANIME_INFO_QUERY, 'variables': id_val})
        
        if req.status_code != 200:
            raise Exception(f"Data post unsuccessful. ({req.status_code})")

        try:
            extracted_data = json.loads(req.text)
        except ValueError or TypeError:
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
                         json={'query': MANGA_INFO_QUERY, 'variables': id_val})
        
        if req.status_code != 200:
            raise Exception(f"Data post unsuccessful. ({req.status_code})")

        try:
            extracted_data = json.loads(req.text)
        except ValueError or TypeError:
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
                         json={'query': STAFF_INFO_QUERY, 'variables': id_val})
        
        if req.status_code != 200:
            raise Exception(f"Data post unsuccessful. ({req.status_code})")

        try:
            extracted_data = json.loads(req.text)
        except ValueError or TypeError:
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
                         json={'query': STUDIO_INFO_QUERY, 'variables': id_val})
        
        if req.status_code != 200:
            raise Exception(f"Data post unsuccessful. ({req.status_code})")

        try:
            extracted_data = json.loads(req.text)
        except ValueError or TypeError:
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
                         json={'query': CHARACTER_INFO_QUERY, 'variables': id_val})
        
        if req.status_code != 200:
            raise Exception(f"Data post unsuccessful. ({req.status_code})")

        try:
            extracted_data = json.loads(req.text)
        except ValueError or TypeError:
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
                          json={'query': REVIEW_INFO_QUERY, 'variables': id_val})

        try:
            extracted_data = json.loads(req.text)
        except ValueError or TypeError:
            return None
        else:
            return extracted_data


    def user_activity(self, page, perpage):
        """
        A Function to get the activity of the currently logged in user.
        :param page: the page of user activity
        :param perpage: number of items on each page
        """
        if self.status == False:
            raise Exception("Current function status is False.")

        token = self.access['token']
        if not token:
            return None
        else:
            headers = {
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json",
                "Accept": "application/json"
            }
            req = requests.post(self.access['apiurl'], headers=headers, json={'query': USER_ID_QUERY, 'variables': {}})
            if req.status_code != 200:
                raise Exception(f"Data post unsuccessful. ({req.status_code})")
            else:
                try:
                    extracted_user = json.loads(req.text)
                    id_val2 = {"id": extracted_user["data"]["Viewer"]["id"], "page": page, "perPage": perpage}
                    req2 = requests.post(self.access['apiurl'], headers=headers, json={'query': USER_INFO_QUERY, 'variables': id_val2})
                    if req2.status_code != 200:
                        raise Exception(f"Data post unsuccessful. ({req.status_code})")
                    else:
                        try:
                            extracted_data = json.loads(req2.text)
                        except ValueError:
                            return None
                        except TypeError:
                            return None
                        else:
                            return extracted_data
                except:
                    return None