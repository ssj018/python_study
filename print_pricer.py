#!/bin/python

import sys
sys.path.extend(["/home/zhoujian/workprj/linux/bin/lib"])
from pyatl import FuturesPriceTable,Symbol
priceTable = FuturesPriceTable("/usr/scratch/pricer/asiafuturespricer.shm")
s = Symbol("pfIFH16")
print priceTable.getPrice(s)
