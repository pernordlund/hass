"""
Script to retrieve bus time from SL-API
"""
import json
import requests
message = 'default'

resource = 'http://api.sl.se/api2/realtimedeparturesv4.json?key=14df1b5b39e744c0ba9d78f0abb89bdc&siteid=4612&timewindow=15'
#resource = data.get('url','not given')
#logger.warning("url {}".format(resource))

resp = requests.get(resource)
if (resp.status_code == 200) and json.loads(resp.text)['ResponseData']:
    for bus in json.loads(resp.text)['ResponseData']['Buses']:
        if bus['Destination'] == 'Slussen':
            message = message + bus['DisplayTime'] + chr(10)
    if not message:
	    message = 'No buses for Slussen within 30 minutes'
else:
   message = 'Error calling SL-api'

print message
#hass.services.call('notify', 'pelles_tfn', { "message" : resource })