#!/usr/bin/python3

import urllib.request
import json
import webbrowser

from pprint import pprint as pp

NASAAPI = 'https://api.nasa.gov/planetary/apod?'
MYKEY = 'api_key=Q9vz7O5oeiZ5sqSH6lzTSJxcnj56oHsr6JrzDnU6'


def main():

    nasaapiobj = urllib.request.urlopen(NASAAPI + MYKEY)

    nasaread = nasaapiobj.read()
    convertedjson = json.loads(nasaread.decode('utf-8'))

    input ("\n This is converted json. Press Enter to continue.")

    pp(convertedjson)

    input("\n This is pretty printed JSON")

    print(convertedjson['explanation'])

    input("\n Press enter to view this photo of the day")
    webbrowser.open(convertedjson['hdurl'])
main()
