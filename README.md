# Simple openVulnAPI Examples
In these examples we're using the Cisco Security API to query for product security advisories. Some of the examples use the API itself with a script and some are using the openVulnQuery tool.

API credentials are pulled from a credentials.json file in the local directory of the scripts/tools. The credentials file looks like this:
``` json
{
  "CLIENT_ID": "YOUR CLIENT ID",
  "CLIENT_SECRET": "YOUR CLIENT SECRET"
}
```

Example usage of the [openVulnAPI](https://developer.cisco.com/psirt/):
``` bash
python critical-adv-this-year.py
```

Example usage of [openVulnQuery](https://github.com/CiscoPSIRT/openVulnAPI/tree/master/openVulnQuery) tool:
``` bash
openVulnQuery --config credentials.json --ios '15.2(4)M5' --json data/ios_15_2.json

openVulnQuery --config credentials.json --advisory cisco-sa-tcl-dos-MAZQUnMF --json data/cisco-sa-tcl-dos-MAZQUnMF.json

openVulnQuery --latest 10 --config credentials.json --json data/latest-10.json
```