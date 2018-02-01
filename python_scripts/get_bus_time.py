"""
Script to retrieve bus time from SL-API
"""
import json
import requests
from datetime import datetime

timewindow = '30'
resourceSL = 'http://api.sl.se/api2/realtimedeparturesv4.json?key=14df1b5b39e744c0ba9d78f0abb89bdc&siteid=4612&timewindow=' + timewindow
resourceHA = 'http://192.168.1.33:8123/api/states/sensor.slussen'
fn = {"friendly_name": "Slussenbuss"} 
errMsg = 'Error calling SL'
noBusMsg = 'No buses for Slussen within ' + timewindow + ' minutes'
message = ''

resp = requests.get(resourceSL)
jsonData = json.loads(resp.text)
if (resp.status_code == 200) and ('ResponseData' in jsonData):
    for bus in jsonData['ResponseData']['Buses']:
        if bus['Destination'] == 'Slussen':
            message = message + bus['DisplayTime'] + chr(10)
    if not message:
	    message = noBusMsg
else:
    time = datetime.now()
    message = time.strftime("%H:%M") + ': ' + errMsg
payload = json.dumps({"state": message, "attributes": {**jsonData,**fn}})
print(payload)

resp = requests.post(resourceHA, data=payload, timeout=1)
#print (resp.text)
#print (payload)