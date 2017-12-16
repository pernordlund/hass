"""
Script to retrieve bus time from SL-API
"""
import json
import requests

resource = redacted
resp = requests.get(resource)

if resp.status_code == 200:
    for bus in json.loads(resp.text)['ResponseData']['Buses']:
	    if bus['Destination'] == 'Slussen':
		    print(bus['DisplayTime'])
