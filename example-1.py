# Example from openVulnQuery readme
from openVulnQuery import query_client
from json import load
with open('credentials.json', 'r') as config:
  creds = load(config)
query_client = query_client.OpenVulnQueryClient(client_id=creds['CLIENT_ID'], client_secret=creds['CLIENT_SECRET'])
advisories = query_client.get_by_year(year=2020, adv_format='default')
for advisory in advisories:
  if advisory.sir == 'Critical':
    print(f"Advisory ID: {advisory.advisory_id}")
    print(f"Advisory SIR: {advisory.sir}")
    print(f"Published: {advisory.first_published}")
    print(f"Advisory Products: {advisory.product_names}")