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


import json
import requests

from constants import *

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
                          json={'query': ANIME_ID_QUERY, 'variables': preset})

        if req.status_code != 200:
            raise Exception(f"Data post unsuccessful. ({req.status_code})")

        try:
            extracted_data = json.loads(req.text)
        except ValueError or TypeError:
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
                          json={'query': CHARACTER_ID_QUERY, 'variables': preset})

        if req.status_code != 200:
            raise Exception(f"Data post unsuccessful. ({req.status_code})")

        try:
            extracted_data = json.loads(req.text)
        except ValueError or TypeError:
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
                          json={'query': MANAGA_ID_QUERY, 'variables': preset})

        if req.status_code != 200:
            raise Exception(f"Data post unsuccessful. ({req.status_code})")

        try:
            extracted_data = json.loads(req.text)
        except ValueError or TypeError:
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
                          json={'query': STAFF_ID_QUERY, 'variables': preset})

        if req.status_code != 200:
            raise Exception(f"Data post unsuccessful. ({req.status_code})")

        try:
            extracted_data = json.loads(req.text)
        except ValueError or TypeError:
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
                          json={'query': STUDIO_ID_QUERY, 'variables': preset})

        if req.status_code != 200:
            raise Exception(f"Data post unsuccessful. ({req.status_code})")

        try:
            extracted_data = json.loads(req.text)
        except ValueError or TypeError:
            return None
        else:
            return extracted_data