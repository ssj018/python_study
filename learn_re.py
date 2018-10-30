#!/usr/bin/env python
# --coding:utf-8--

import re

strings = 'edijhbh32498bvahjdsbfpqhreuilbnv'

r = re.search('[0-9]', strings)

print r.string
