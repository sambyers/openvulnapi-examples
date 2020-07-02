# Example of critical advisories for current year
from openvulnapi import openVulnAPI
from json import dumps
from datetime import date

year = str(date.today().year)
api = openVulnAPI()
advisories = api.get_advisories_by_year(year)
critical_advisories = [advisory for advisory in advisories if advisory['sir'] == 'Critical']
with open(f'data/{year}-critical.json', 'w') as file:
  file.write(dumps(critical_advisories, indent=4))