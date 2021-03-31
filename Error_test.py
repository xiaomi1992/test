# -*- coding: utf-8 -*-
'''
@time   2021-3-16
@Author:xiaomi
'''

from urllib import request,error
try:
    response = request.urlopen('http://cuiqingcai.com/index.html')
except error.HTTPError as e:
    print(e.reason, '\n', e.code, '\n', e.headers, )
except error.URLError as e:
    print(e.reason)
else:
    print('Request successfully')