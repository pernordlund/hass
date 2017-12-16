"""
Script to retrieve bus time from SL-API
"""
#import json
#import requests
message = ''

resource = data.get('url','not given')
logger.warning("url {}".format(resource))

#resp = requests.get(resource)
#if (resp.status_code == 200) and json.loads(resp.text)['ResponseData']:
#    for bus in json.loads(resp.text)['ResponseData']['Buses']:
#        if bus['Destination'] == 'Slussen':
#            message = message + bus['DisplayTime'] + chr(10)
#    if not message:
#	    message = 'No buses for Slussen within 30 minutes'
#else:
#    message = 'Error calling SL-api'

hass.services.call('notify', 'pelles_tfn', { "message" : resource })