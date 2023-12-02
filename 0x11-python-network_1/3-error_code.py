#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL
    and displays the body of the response (decoded in utf-8).
"""

import sys
from urllib import request, error

if __name__ == "__main__":
    url = sys.argv[1]

    my_request = request.Request(url)
    try:
        with request.urlopen(my_request) as response:
            print(response.read().decode("ascii"))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
