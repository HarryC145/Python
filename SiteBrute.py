import os, requests, sys
from os import path
topnumber = 300000
found = 0
currentnumber = 200000
while currentnumber <= topnumber:
    checked = '{:06d}'.format(currentnumber)
    url = "http://xx" + checked + ".xxxxxxxxx.net"
    request = requests.get(url, allow_redirects=False)
    if request.status_code == 200:
        SitePresent = open("present.txt", "a")
        SitePresent.write(url + '\n')
        SitePresent.close()
        print('I found a site, at', url)
        found = found + 1
        print(found)
    if request.status_code == 301:
        print('I looked for a site at', url, 'and I did not see anything')
        notfound = open("notfound.txt", "a")
        notfound.write(url + '\n')
        notfound.close()
    currentnumber = currentnumber + 1
