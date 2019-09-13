#! /usr/bin/python
"""This script sends zabbix alerts to rocketchat.

1. Place this script in /usr/lib/zabbix/alertscripts
2. Give zabbix user permissions to execute the script.
3. Create new "Media Type" under "Administration" Tab of type script.
4. Add 3 script parameters: {ALERT.SENDTO}, {ALERT.SUBJECT} and {ALERT.MESSAGE}
5. Set a user to use this Media Type and set it's sendto parameter the webhook
for rocketchat.
"""

import requests
import sys

url = sys.argv[1]
if "Resolved" in sys.argv[2]:
    subject = ":tropical_drink: " + sys.argv[2] + " :beer:"
else:
    subject = ":bomb: " + sys.argv[2] + " :bomb:"

message = sys.argv[3]

payload = {"text": subject + "\n" + message + "\n"}
r = requests.post(url, json=payload)
