#!/usr/bin/python3

import requests
def main():
    neourl = 'https://api.nasa.gov/neo/rest/v1/feed?'
    startdate =  'start_data=2018-06-01'
    enddate = '&end_date=END_DATE'
    mykey = '&api_key=Q9vz7O5oeiZ5sqSH6lzTSJxcnj56oHsr6JrzDnU6'

    neourl = neourl + startdate + mykey

    neourlobj = urllib.request.urlopen(neourl)

    neoread = neourlobj.read()

    decodeneo = json.loads(neoread.decode('utf-8'))

print("\n\nConverted python data")

print(decodeneo)


#input ("\n Press Enter to open NASA picture of the day in Firefox")

#webbrowser.open(decodeapod['url'])
