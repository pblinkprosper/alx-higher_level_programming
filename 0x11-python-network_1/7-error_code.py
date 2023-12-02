#!/usr/bin/python3
"""Python script that takes in a URL, sends a request
    to the URL and displays the body of the response.
"""
import requests
import sys

if __name__ == "__main__":
    req = requests.get(sys.argv[1])
    reqstat_code = req.status_code
    if reqstat_code > 400:
        print('Error code: {}'.format(reqstat_code))
    else:
        print('{}'.format(req.text))
