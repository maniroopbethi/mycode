#!/usr/bin/python3

import urllib.request
import json
import webbrowser

apodurl = 'https://api.nasa.gov/planetary/apod?'
mykey = 'api_key=Q9vz7O5oeiZ5sqSH6lzTSJxcnj56oHsr6JrzDnU6'

apodurlobj = urllib.request.urlopen(apodurl + mykey)

apodread = apodurlobj.read()

decodeapod = json.loads(apodread.decode('utf-8'))

print("\n\nConverted python data")

print(decodeapod)


input ("\n Press Enter to open NASA picture of the day in Firefox")

webbrowser.open(decodeapod['url'])
