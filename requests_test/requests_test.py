# -*- coding: utf-8 -*-
'''
@time   2021-3-19
@Author:xiaomi
'''

import requests

r = requests.get('http://httpbin.org/get')
print(type(r.text))
print(r.json())
print(type(r.json()))
