#http://maps.googleapis.com/maps/api/geocode/json?address=faridabad

import urllib.request, urllib.response, urllib.error
import json

serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'
count=0
while count==0:
    count=count+1
    address = input('Enter location: ')
    if len(address)<1: break

    url=serviceurl+urllib.parse.urlencode(
        {'address':address})

    print("Retrieving URL is:" , url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js=json.loads(data)
    except:
        js=None
    if not js or 'status' not in js or js['status']!='OK':
        print("====Failure to retrieve=====")
        print(data)
        continue

  #  print(json.dumps(js, indent=4))
    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)

