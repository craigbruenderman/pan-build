#!/usr/local/bin/python

import pan.xapi
from datetime import datetime
import xml.etree.ElementTree as ET
import sys
import os
import getopt
import re
import json
import pprint
import logging

## To generate API key
## https://hostname/api/?type=keygen&user=username&password=password

user = 'admin'
password = ''
hostname = 'pa-200'
keygen = False

try:
    xapi = pan.xapi.PanXapi(tag=None, api_username=user, api_password=password, hostname=hostname)

except pan.xapi.PanXapiError as msg:
    print('pan.xapi.PanXapi:', msg)
    sys.exit(1)

xpath = "/config/devices/entry/vsys/entry/rulebase/security"
xapi.show(xpath=xpath)
s = xapi.xml_result()
tree = ET.fromstring(s)

for child in tree.iter('entry'):
    rule_name = child.get('name')
    nodes = child.findall('from')
    for node in nodes:
        from_int = node.find('member').text
        print rule_name, from_int

#print(s.lstrip('\r\n').rstrip())
