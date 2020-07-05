import requests
from json import loads

class openVulnAPI:
  def __init__(self, baseurl, authzurl, client_id, client_secret):
    self.baseurl = baseurl
    self.authzurl = authzurl
    self.client_id = client_id
    self.client_secret = client_secret
    self.token = self.get_oauth_token()
    self.response = None

  def get_oauth_token(self):
      r = requests.post(
          self.authzurl,
          params={'client_id': self.client_id, 'client_secret': self.client_secret},
          data={'grant_type': 'client_credentials'}
      )
      r.raise_for_status()
      return r.json()['access_token']

  def get_request(self, path, params=None):
    headers = {
      'Authorization': f'Bearer {self.token}',
      'Accept': 'application/json'
    }
    request_data = {
              'url': f'{self.baseurl}{path}',
              'headers': headers,
              'params': params,
          }
    r = requests.get(**request_data)
    r.raise_for_status()
    self.response = r
    return r.json()

  def get_advisories_by_year(self, year):
    path = f'advisories/year/{year}'
    r = self.get_request(path)
    return r['advisories'] # Returns list of dictionaries by taking off outer dictionary