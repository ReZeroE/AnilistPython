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

import sys
import os
import json
import pkg_resources
import re


class Setup:
    def __init__(self):
        self.required_lib = {
            'numpy': 0,
            'pytest': 0,
            'requests': 0
        }

        self.setup_var = self.setup_lib()


    def setup_lib(self):

        d = dict()
        try:
            with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'setup.json'), 'r', encoding="utf-8") as rf:
                d = json.load(rf)
        except Exception as e:
            pass
            # print('Setup file error.')


        if d['setup'] == 0:
            control = self.download_lib()
        else:
            for lib, dow in d.items():
                if dow == 0:
                    control = self.download_lib()
            
        d = dict((k, 0) for k, v in d.items())

        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'setup.json'), 'w') as wf:
            json.dump(d, wf, indent=4)

    def download_lib(self):
        required = {lib.lower() for lib, dow in self.required_lib.items()}
        installed = {pkg.key for pkg in pkg_resources.working_set}
        missing = required - installed

        if missing:
            import subprocess

            print(f"Warning: Required Libraries Missing >>> {missing}")
            user_input = input("Initiate automatic library installation? Proceed [y/n]")

            if user_input.lower() == 'n':
                print("Program Terminated...")
                sys.exit(0)
            elif user_input.lower() == 'y':
                print("Installing required libraries...")
                for lib in missing:
                    subprocess.run(f"py -{self.get_python_version()} -m pip install {lib}", shell=True)
                    print(f"Library >{lib}< has been installed. Please restart the program.")
                    sys.exit(0)
            else:
                print("User input unrecognized. Program terminated...")
                sys.exit(0)

            return True # has missing lib (lib installed)
        return False # no missing lib


    def validate_installation(self):
        required = {lib.lower() for lib, dow in self.required_lib.items()}
        installed = {pkg.key for pkg in pkg_resources.working_set}
        missing = required - installed

        
        if missing:
            print(f"Libraries {missing} failed to be installed. Program Terminated.")
            sys.exit(0)
        else:
            print("Library validation complete. All required Libraries has been sucessfully installed.")

    def get_python_version(self):
        from platform import python_version
        ret = re.match('[0-9].[0-9]', python_version())
        return ret.group(0)


if __name__ == '__main__':
    import time

    start = time.time()
    s = Setup()
    s.setup_lib()
    print(time.time() - start)