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
import sys
import urllib.request

class DatabaseUpdateTool():
    def download_new_db(self):
        """
        Download new database from Github.
        """
        DATABASE_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "databases")
        urllib.request.urlretrieve(
            ## DOWNLOAD FROM:
            "https://github.com/ReZeroE/AnilistPython/blob/dev/AnilistPython/databases/anime_database.sqlite3?raw=true", 
            
            ## TO DIRECTORY:
            os.path.join(DATABASE_DIR, "anime_database.sqlite3")
        )

    def update_db(self, verbose=True):
        """
        Driver function for updating the local anime database.
        :param verbose: verbose error, default to True
        """
        try:
            self.download_new_db()
        except Exception as e:
            if verbose:
                print(f"ERROR: Database failed to be updated.\n{e}", file=sys.stderr)


if __name__ == "__main__":
    d = DatabaseUpdateTool()
    d.update_db()




