#!/usr/bin/env python
#--coding: utf-8 --

import threading
import time

class MyThread(threading.Thread):
    def __init__(self,n,sleep_time):
        super(MyThread,self).__init__()
        self.n = n
        self.sleep_time=sleep_time
    def run(self):# in super class  the methon start() will call the run(). I rewrite the run() methon here. the name must be run()
        print("run task %d\n thread:%s \n"%(self.n,threading.current_thread()))
        time.sleep(self.sleep_time)
        print("work done !")

#t1=MyThread(1)
#t2=MyThread(2)

#t1.start()
#t2.start()
t_list=[]
start_time=time.time()
for i in range(10):
    t = MyThread(i,i)
    t.setDaemon(True)# if a thread set as a daemon , the main process will not wait it by default. if it not work done when main process exit, it will be killed
    t.start()
    t_list.append(t) 

#for t  in t_list:
#    t.join()
    
time.sleep(4)
print("cost= %f \n thread:%s \n   threads  count:%d "%(time.time()-start_time,threading.current_thread(),threading.active_count())) #this is ok
#print ("cost =",time.time()-start_time # this is in  python3
