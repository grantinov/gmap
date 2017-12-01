"""
The objective for findfile is to ...

 Project Name: gmap
 Developed by grant.stokley
 Date:    12/01/2017
 Time:    09:10


Example usage(s):
# python findfile.py [path] [file]
# python findfile.py /Users/grant.stokley/Documents/repos *.py
# python findfile.py ./ *.pdf

"""

import fnmatch
import os
import sys


matches = []
for root, dirnames, filenames in os.walk(sys.argv[1]):
    for filename in fnmatch.filter(filenames, sys.argv[2]):
        matches.append(os.path.join(root, filename))
        print(os.path.join(root, filename))