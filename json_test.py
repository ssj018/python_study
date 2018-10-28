#!/usr/bin/python  env
#--coding:UTF-8--

import json

data = {
'hostname' : 'zues1',
'IP': "10.1.32.5",
'User': 'root',
'Password':  'q1w2E#R$'
}


# obj = [[1,2,3],123,123.123,'abc',{'key1':(1,2,3),'key2':(4,5,6)}]
# encodedjson = json.dumps(obj)
# print repr(obj)
# print encodedjson


json_str = json.dumps(data)
print json_str
print data
