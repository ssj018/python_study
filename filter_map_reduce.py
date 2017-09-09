#!/usr/bin/env python
#--coding:utf-8--

import sys

class mymath(object):

    def __init__(self):
        pass

    def div_filter(self,n,data):
    #find  the number in  data which can be divisable by n
        def div_n(x):
            return x%n == 0
        return filter(div_n,data)

    def cube(self,data):
    # find the cube of the number in data 
        def cube_x(x):
            return x*x*x
        return map(cube_x,data)

    def factorial(self,number):
    # find the factorial of number 
        if number < 1:
            print "number must larger than 0"
            sys.exit(1)
        def factorial_n(x,y):
            return x*y
        return reduce(factorial_n,range(1,number),1)#if the range just 1 , need a default value to be the value for the args : "y"     
if __name__ == "__main__":
    m=mymath()
    data=m.div_filter(3,range(1,33))
    print data
    data2=m.cube(range(1,30))
    print data2 
    data3=m.factorial(1)
    print data3
