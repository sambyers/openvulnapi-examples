# openVulnAPI-Examples
Example usage of the [openVulnAPI](https://developer.cisco.com/psirt/)

```
openVulnQuery --config credentials.json --ios '15.2(4)M5' --json ios_15_2.json

openVulnQuery --config credentials.json --advisory cisco-sa-tcl-dos-MAZQUnMF --json cisco-sa-tcl-dos-MAZQUnMF.json

openVulnQuery --latest 10 --config credentials.json --json latest-10.json
```