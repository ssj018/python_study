#!/usr/bin/env python

import threading
import time

def run1(n):
    semaphore.acquire()
    time.sleep(2)
    print  "thread %d \n"%n
    semaphore.release()

semaphore=threading.BoundedSemaphore(5)

for  i  in range(33):
    t = threading.Thread(target=run1,args=(i,))
    t.start()
