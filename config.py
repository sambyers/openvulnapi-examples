'''
Config for openvulnapi class
'''
from json import loads
from os import path

# openVulnAPI URL and oauth URL
apiurls = { 
  'baseurl': 'https://api.cisco.com/security/',
  'authzurl':'https://cloudsso.cisco.com/as/token.oauth2'
}
if path.exists('credentials.json'):
  # Use a credentials.json file for your credentials
  with open('credentials.json', 'r') as config:
    apicredentials = loads(config.read())
else:
  # Or set your credentials here
  apicredentials = {
    'client_id': 'YOUR CLIENT ID',
    'client_secret': 'YOUR CLIENT SECRET'
  }
apiargs = {**apicredentials, **apiurls}