#!/usr/bin/python3

import urllib.request
import json
import turtle


## Trace the ISS - earthorbital space station
eoss = 'http://api.open-notify.org/iss-now.json'

## call the webserv

trackiss = urllib.request.urlopen(eoss)

#put into file object

ztrack = trackiss.read()

## json2 python data structure

result = json.loads(ztrack.decode('utf-8'))

## display our pythonic data

print("\n\nConverted python data")
print(result)
input("\nISS data retrieved & converted. Press any key to continue")

location = result['iss_position']
lat = location['latitude']
lon = location['longitude']
print('\nLatitude:', lat)
print('Longitude:',lon)

screen = turtle.Screen()
screen.setup(720, 360)

screen.setworldcoordinates(-180,-90,180,90)

screen.bgpic('iss_map.gif')

screen.register_shape('spriteiss.gif')
iss = turtle.Turtle()
iss.shape('spriteiss.gif')
iss.setheading(90)

lon = round(float(lon))
lat = round(float(lat))
iss.penup()
iss.goto(lon, lat)

### My location

yellowlat =  39.1
yellowlon =  77.2
mylocation = turtle.Turtle()
mylocation.penup()
mylocation.color('yellow')
mylocation.goto(yellowlon,yellowlat)
mylocation.dot(5)
mylocation.hideturtle()

passiss ='http://api.open-notify.org/iss-pass.json'
passiss = passiss + '?lat=' + '&lon=' + str(yellowlon)
response = urllib.request.urlopen(passiss)
result = json.loads(response.read().decode('utf-8'))

over = result['response'][1]['risetime']


turtle.mainloop()
