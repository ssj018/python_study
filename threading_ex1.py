#!/usr/bin/env python
#--coding:utf-8--


import threading
import time


def run(n):
   print("this is task: %d" % n)
   time.sleep(2)


t1 = threading.Thread(target=run, args=(1,))
t2 = threading.Thread(target=run, args=(2,))
t3 = threading.Thread(target=run, args=(3,))
t4 = threading.Thread(target=run, args=(4,))
t5 = threading.Thread(target=run, args=(5,))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()

