__author__ = 'anna'

import urllib
import json

service_url='http://python-data.dr-chuck.net/geojson?'
while True:
    university=raw_input("Enter university:")
    url=service_url+urllib.urlencode({"sensor":"false","address":university})
    print "Retrieving", url
    urlh=urllib.urlopen(url)
    urlstr=urlh.read()

    try: js=json.loads(urlstr)
    except: js=None
    if "status" not in js or js["status"] != "OK":
        print "Failure to retrieve", url


    try:place_id=js["results"][0]["place_id"]
    except: continue
    break


print "Place id:", place_id



