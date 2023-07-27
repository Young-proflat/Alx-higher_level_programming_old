#!/usr/bin/python3

""" Accept url and send a request url
and display the body of the response 
with the error code
"""
import sys
import urllib.error
import urllib.request

if "__name__" == "__main__":
    url = sys.argv[1]
    request = urllib.request.Request(url)

    try:
        with urllib.request.urlopen(request) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
