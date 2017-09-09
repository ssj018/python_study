#!/usr/bin/python
#--coding:UTF-8--

import yaml


#data=[{"user":[[ {"id_0":"root"}],[{"id_1000":"mds"}],[{"id_300":"atl"}]] }, {"password":"q1w2E#R$"},{"IP":[{"eno1":"10.1.74.32"},{"eon2":"192.168.10.20"}]}]
data=[{"user":[ {"id_0":"root"},{"id_1000":"mds"},{"id_300":"atl"}] }, {"password":"q1w2E#R$"},{"IP":[{"eno1":["10.1.74.32","10.1.74.33"]},{"eon2":"192.168.10.20"}]}]
#data=[{"user":[ {"id_0":["root","shuangjian"]},{"id_1000":"mds"},{"id_300":"atl"}] }, {"password":"q1w2E#R$"},{"IP":[{"eno1":["10.1.74.32","10.1.74.33"]},{"eon2":["192.168.10.20"]}]}]
#data=[{"user":[ {"id_0":["root","shuangjian"]},{"id_1000":"mds"},{"id_300":"atl"}] }, {"password":["q1w2E#R$"]},{"IP":[{"eno1":["10.1.74.32","10.1.74.33"]},{"eon2":["192.168.10.20"]}]}]
#with open("config_yaml/shfe.yml","r") as f:
#  data = yaml.load(f)

with open("config_yaml/host.yml","r") as f:
  host = yaml.load(f)
print type(host)
def print_yml(data):
#print data
  for i in  data:
    print i+":\n"
    # print i
    for a in data[i]:
      if type(data[i]) is list:
      	print a
      elif type(data[i]) is dict:
  	print a,data[i][a]  
#  	print type(data[i][a])
      else:
  	print "do nothing"
    print ""
	
def dump_yml(data,d_file):
  with open("config_yaml/"+d_file,"w") as f:
    #yaml.dump(data,f)
    yaml.dump_all(data,f,default_flow_style=False)

print_yml(host)
dump_yml(data,"data.yml")
