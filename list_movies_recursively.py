#!/usr/bin/env python
#--coding:utf-8--

import yaml
import argparse

def list_movies(movies,indent=False,level=0):
   for item in movies:
      if isinstance(item,list):
         level +=1
         list_movies(item,indent,level)
      else:
         #print " "*level+str(item)
         if indent :
             for tab_stop in range(level):
                print "\t",# in 3.0 print("\t",end=' ')
         print(item)




if __name__ == "__main__":
   parse = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
#  group = parse.add_argument_group() ## this is different from  "add_mutually_exclusive_group"
   parse.add_argument('-f','--c_file',required=True,help="the file of movies")
   parse.add_argument('-l','--level',default=0,type=int,help="the level of suojin")
   parse.add_argument('-i','--indent',action='store_true',help='if you need the indent')
   args = parse.parse_args()

   with open(args.c_file,"r") as f:
      data=yaml.load(f)
   
   list_movies(data,args.indent,args.level)
