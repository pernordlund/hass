"""
Script to retrieve bus time from SL-API
"""
import json
import requests
from datetime import datetime
message = 'default'

resourceSL = 'http://api.sl.se/api2/realtimedeparturesv4.json?key=14df1b5b39e744c0ba9d78f0abb89bdc&siteid=4612&timewindow=15'
resourceHA = 'http://192.168.1.33:8123/api/states/sensor.slussen'

resp = requests.get(resourceSL)
jsonData = json.loads(resp.text)
if (resp.status_code == 200) and ('ResponseData' in jsonData):
    for bus in jsonData['ResponseData']['Buses']:
        if bus['Destination'] == 'Slussen':
            message = message + bus['DisplayTime'] + chr(10)
    if not message:
	    message = 'No buses for Slussen within 30 minutes'
else:
   message = 'Error calling SL-api'

#payload = '{"state": "ssKlisatra", "attributes": {"Bus 1": \"' + message + '\",' + \
#    '"Bus2": \"' + str(datetime.now()) + '\"}}'
payload = json.dumps(jsonData)

resp = requests.post(resourceHA, data=payload)