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
import json
import urllib.request
from datetime import date

class _DatabaseUpdateTool:
    """
    AnilistPython anime database update handler class.
    Provides functions for automatically triggering or manual local DB update.
    """

    def __init__(self, auto_update=True):
        # Triggers automatic update
        if (auto_update == True) and (self.trigger_update() == True):
            self.update_db()

    def download_new_db(self):
        """
        Download new database from Github.
        """
        DATABASE_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "databases")
        urllib.request.urlretrieve(
            ## DOWNLOAD FROM:
            "https://github.com/ReZeroE/AnilistPython/blob/dev/AnilistPython/tmp/anime_database_tmp.sqlite3?raw=true", 
            
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


    def trigger_update(self):
        """
        Triggers automatic database update.
        """
        # Update database every 30 days
        UPDATE_INTERVAL = 30

        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "db_status.json"), "r") as rf:
            f = json.load(rf)

        # Find days bewteen today and the last updated date
        today = date.today()
        last_updated_at = f['last_updated_at']
        mdy = last_updated_at.split("/")
        last_updated_at = date(int(mdy[2]), int(mdy[0]), int(mdy[1]))

        if (today - last_updated_at).days > UPDATE_INTERVAL:
            strtime = today.strftime("%m/%d/%Y")
            d = dict()

            d["last_updated_at"] = strtime
            with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "db_status.json"), "w") as wf:
                jobj = json.dumps(d, indent=2)
                wf.write(jobj)
            return True
        else:
            return False
            

if __name__ == "__main__":
    d = _DatabaseUpdateTool()
    # d.update_db()
    # d.trigger_update()



