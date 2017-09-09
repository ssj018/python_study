#!/usr/bin/env python
#--coding: utf-8 --

import threading
import time

class MyThread(threading.Thread):
    def __init__(self,n,lock):
        super(MyThread,self).__init__()
        self.n = n
        #self.num=num # this is shili variable
        self.lock=lock
    def run(self):# in super class  the methon start() will call the run(). I rewrite the run() methon here. the name must be run()
        self.lock.acquire_lock()
        global num #access the glabal variable 
        num += 1
        #time.sleep(1)  #can not sleep here,will not relase the lock. the other programe will wait ...
        self.lock.release()
        time.sleep(1.5)
#        print num
        #print self.num
    #    return self.num
    #def print_num(self):
num=1000
lock=threading.Lock()
t_list=[]
start_time=time.time()
for i in range(10):
    t = MyThread(i,lock)
    t.start()
    t_list.append(t) 

for t  in t_list:
    t.join()


#for t in t_list:
#    print  t.num

print num
#print("cost= %f \n thread:%s \n   threads  count:%d "%(time.time()-start_time,threading.current_thread(),threading.active_count())) #this is ok
#print ("cost =",time.time()-start_time # this is in  python3
