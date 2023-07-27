#!/usr/bin/python3
""" Takes in a url and email 
Post and request passed in the url
"""

import sys
import urllib.parse
import urllib.request

if "__name__" == "__main__":
    url = sys.argv[1]
    value = {"email" sys.argv[2]}
    data = urllib.parse.urlencode(value).encode("ascii")

    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
    
