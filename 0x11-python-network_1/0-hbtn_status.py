#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""

from urllib import request

req = 'https://alx-intranet.hbtn.io/status'
with request.urlopen(req) as response:
    response = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(response)))
    print("\t- content: {}".format(response))
    print("\t- utf8 content: {}".format(response.decode(encoding='utf-8')))
