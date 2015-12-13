# This is a script that is going to format your URL's for you so that you can import them to the scanners easily
# Created by Harry Cross - me@harrycross.me HarryCross on Freenode and HCross on EFnet

# Import all the libraries and things we need
import os
import re
import ast
import sys
import shutil
import urllib
from test.dis_module import f

# Set the argument we get from the user as a variable

FileName = sys.argv[1]

# Now we have declared everything, open the text file and then open a new one to print into
file = open(FileName, 'r')
for URL in file:
    if re.search(r'ftp:\/\/[^\/]+/', URL) and re.search(r'ftp://', URL):
        URL = URL[6:-2]
        Results = open("Results.txt","a")
        Results.write(URL + '\n')
        Results.close()
        print(URL)
file.close()  
