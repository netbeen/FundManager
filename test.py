#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request
import json

response = urllib.request.urlopen('http://fund.eastmoney.com/f10/F10DataApi.aspx?type=lsjz&code=160119&page=3&per=20&sdate=&edate=&rt=0.9175347448326647')
html = response.read().decode('gb2312')
print(html)
apiData = html[12:-1]
print(apiData)
testJson = {"name" : "YY", "age" : 2}
jsonData = json.loads(testJson)
