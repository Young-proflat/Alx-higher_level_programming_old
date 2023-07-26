#!/usr/bin/python3
"This script fetches a urllib for this url"

if "__name__" == "__main__":
    import urllib.request

    url = "https://alx-intranet.hbtn.io/status"

    with urllib.request.urlopen(url) as response:
        html = response.read()


    print("\tBody reponse:")
    print("\ttype: {}" .format(type(html)))
    print("\t -content: {}".format (html))
    print("\t -utf8 content: {}".format(html.decode('utf8')))
