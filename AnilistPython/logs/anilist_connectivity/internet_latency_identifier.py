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


import urllib.error as ue
import urllib.request as ur

class InternetChecker:
    '''
        Identifies the internet status of the user. Prompts the user to use the provided local database if their
        internet latency is too high.
    '''
    def internet_latency_check(self) -> bool:
        '''
            Attempts to access google.com with an one second timeout theshold.
            :rtype: bool
        '''
        try:
            s = ur.urlopen("http://www.google.com", timeout=1)
            return True
        except ue.URLError as ex:
            return False

if __name__ == "__main__":
    ic = InternetChecker()
    print(ic.internet_latency_check())