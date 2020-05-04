#!/usr/bin/env python3
import sys
import os
import argparse
import re
import requests
import hashlib
import collections
import html2text


class IdiotSurf:
    def __init__(self, cachedir):
        self.cachedir = cachedir
        if not os.path.exists(cachedir):
            os.mkdir(cachedir)
        os.chdir(cachedir)
        self.cachestack = collections.deque()
    
    def is_url(self, url):
        url_pattern = re.compile(
            r'^(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?$')
        if re.match(url_pattern, url):
            return True
        return False

    def showpage(self, content):
        rendered = html2text.html2text(content)
        print(rendered)

    def savetocache(self, url, content):
        hashobj = hashlib.md5(url.encode())
        filename = hashobj.hexdigest()
        with open(filename, 'w') as f:
            f.write(content)
    
    def opencache(self, url):
        hashobj = hashlib.md5(url.encode())
        filename = hashobj.hexdigest()
        with open(filename) as f:
            content = f.read()
        self.showpage(content)

    def gotourl(self, url):
        if not (url.startswith('http://') or url.startswith('https://')):
            url = 'http://' + url
        req = requests.get(url)
        if req:
            return req.text
        return 'Error: ' + req.status_code

    
    def mainloop(self):
        print('''
            Welcome to IdiotSurf, the most useless web browser ever made
            - Type the URL and then ENTER to browse
            - Type back to back to previous page
            - Type exit or quit to exit
            ''')
        lasturl = ''
        patience = 3 # patience level, just for fun
        while True:
            print('>', end=' ')
            userinput = input()
            if userinput.lower() in ['quit', 'exit']:
                sys.exit()
            elif self.is_url(userinput):
                if lasturl:
                    self.cachestack.append(lasturl)
                content = self.gotourl(userinput)
                self.showpage(content)
                self.savetocache(userinput, content)
                lasturl = userinput
            elif userinput.lower() == 'back':
                if len(self.cachestack):
                    self.opencache(self.cachestack.pop())
            else:
                if patience == 0: # even a computer has its limit...
                    print('JANCUK RAIMU ASU!!!!!! KOWÉ ISO NGANGGO KOMPUTER OPO ORA TOH NDÉS???')
                    sys.exit(69)
                print('What the fuck is it supposed to mean?')
                patience -= 1


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