#!/usr/bin/python3
 import sys
 import urllib.request

 "script print an header value using the urllib"
  if "__name__" == "__main__":

      url = sys.argv[1]:
          with urllib.request.urlopen (url) as response:
              headers = response.info()
              X-Request-Id = headers['X-Request-Id']
        
        print(X-Request-Id)
