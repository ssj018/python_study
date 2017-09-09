#!/usr/bin/env python
#--coding: utf-8 --

import threading
import time

class MyThread(threading.Thread):
    def __init__(self,n,num):
        super(MyThread,self).__init__()
        self.n = n
        self.num=num # this is shili variable
    def run(self):# in super class  the methon start() will call the run(). I rewrite the run() methon here. the name must be run()
        global num #access the glabal variable 
        num+= 1
        print num
        #print self.num
    #    return self.num
    #def print_num(self):
num=0
t_list=[]
start_time=time.time()
for i in range(10):
    t = MyThread(i,num)
#    t.setDaemon(True)# if a thread set as a daemon , the main process will not wait it by default. if it not work done when main process exit, it will be killed
    t.start()
    t_list.append(t) 

for t  in t_list:
    t.join()


for t in t_list:
    print  t.num
#print("cost= %f \n thread:%s \n   threads  count:%d "%(time.time()-start_time,threading.current_thread(),threading.active_count())) #this is ok
#print ("cost =",time.time()-start_time # this is in  python3
