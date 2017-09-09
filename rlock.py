#!/usr/bin/env python
#--coding:utf-8--

import threading
import time

#lock=threading.Lock()
lock = threading.RLock()
num1,num2 = 0 , 0
def run1():
    print "111"#only can excu 1 time , then will be lock
    lock.acquire()#when require the lock .must wait for run3 release the lock. but run3 canot release the lock. so programe  blocked here
    global num1
    num1 += 1
    lock.release()
    print num1
    return 

def run2():
    lock.acquire()
    global num2
    num2 += 1
    lock.release()
    print num2
    return

def run3():
    #lock.acquire_lock() RLOCK has no this attribute 
    time.sleep(1)
    lock.acquire()
    res1=run1()
    print ("==============")
    res2=run2()
    lock.release()

for i in range(10):
    t = threading.Thread(target=run3)
    t.start()

#time.sleep(1)
 
while threading.active_count()!=1:
    print ("still runing \n %d  child threads "%(threading.active_count() -1))
    time.sleep(0.5)
else:
    print ("all threads has  done")
    print num1 ,num2
