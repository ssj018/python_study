#!/usr/bin/env python
#--coding:UTF-8--

import os

path1='c:\\abc\def'
path2='//123\\456'
dir1='aa\\bb'
a=[]
a.append(path1)
a.append(path2)
a.append(dir1)



#print a[0]
#print a[1]
print a[2]
dir2=a[2]
print os.getcwd()
print dir2
os.chdir(a[2])
os.listdir(".")
#os.listdir(a[2])
