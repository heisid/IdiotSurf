#!/usr/bin/env python3
import sys
import os
import argparse
import re
import requests


class IdiotSurf:
    def __init__(self, cachedir):
        self.cachedir = cachedir
        if not os.path.exists(cachedir):
            os.mkdir(cachedir)
        os.chdir(cachedir)
    
    def is_url(self, url):
        url_pattern = re.compile(
            r'^(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?$')
        if re.match(url_pattern, url):
            return True
        return False

    def showpage(self, url):
        pass
    
    def mainloop(self):
        print('''
            Welcome to IdiotSurf, the most useless web browser ever made
            - Type the URL and then ENTER to browse
            - Type back to back to previous page
            - Type exit or quit to exit
            ''')
        while True:
            print('>', end=' ')
            userinput = input()
            if userinput.lower() in ['quit', 'exit']:
                sys.exit()
            elif self.is_url(userinput):
                self.showpage(userinput)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Useless Text Based Browser')
    parser.add_argument(
        '-d', '--cache-directory', action='store', dest='cachedir',
        help='Directory to save cached web pages')
    args = parser.parse_args()
    if args.cachedir:
        cachedir = args.cachedir
    else:
        cachedir = 'idiotdir'

    browser = IdiotSurf(cachedir)
    browser.mainloop()