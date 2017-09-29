#! /bin/python

import sys
import re
import datetime
import time
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import numpy
import random


def timeofday(timeStr):
	timeA = datetime.datetime.strptime(timeStr, "%H:%M:%S.%f")
	return timeA

if __name__ =="__main__":
	if (len(sys.argv) < 3 or (sys.argv[1].lower() != 'ask' and sys.argv[1].lower() != 'bid')):
		print "Usage: " + sys.argv[0] + " <bid|ask> file1 file2 file3 ..."
		print " fileformat: "
		print "\t time bidprice askprice"
		exit(1)

	side = sys.argv[1].lower()
	files = []	
	timeArrs = []
	bidArrs = []
	askArrs = []
	for filename in sys.argv[2:]:
		fp = open(filename, 'r')
		line = None
        	timeArr = []
        	bidArr = []
        	askArr = []
		while True:
                	line = fp.readline();
                	if not line:
                        	break;
                	list = line.split()
                	time, bid, ask= list[0:3]
                	timeArr.append(timeofday(time))
                	bidArr.append(bid)
                	askArr.append(ask)
        	fp.close()
		files.append(filename)
		timeArrs.append(timeArr)
		bidArrs.append(bidArr)
		askArrs.append(askArr)

	timeStart = datetime.datetime.strptime("09:00:00.0", "%H:%M:%S.%f")
	timeEnd = datetime.datetime.strptime("15:30:00.0", "%H:%M:%S.%f")
	plt.figure(figsize=(30,15))
	ax = plt.gca()
	ax.set_xlim( [ timeStart, timeEnd ] )
	colors = ['r', 'b', 'g', 'c', 'm', 'y', 'k', 'w']
	title = ""
	for index in range(len(files)):
		if side == "ask":
			plt.plot(timeArrs[index], askArrs[index], color=colors[len(files) - 1 - index], label=files[index])
		else:
			plt.plot(timeArrs[index], bidArrs[index], color=colors[len(files) - 1 - index], label=files[index])
	
		if index == len(files) - 1:
			title = title + files[index]
		else:
			title = title + files[index] + " vs. "
	title = title +"(" + side + ")"
	legend = plt.legend(loc='upper right', shadow=True)
	plt.title(title)
	plt.savefig(title + ".jpg")
	plt.show()


