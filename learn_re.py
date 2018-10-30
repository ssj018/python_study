#!/usr/bin/env python
# --coding:utf-8--

import re

strings = 'edijhbh32498bvahjdsbfpqhreuilbnv'

r = re.findall('[0-9]', strings)

print "there are thoese numbers:"
for i in r:
    print i
