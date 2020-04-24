#!/usr/bin/python
# -*- coding: utf-8 -*- 
import os,sys,re
from pydub.utils import mediainfo
import datetime
import csv
ROOT = os.path.join(os.environ['HOME'], 'Desktop/表格.csv')
x=1
PATH = sys.argv[1]

out = open(ROOT,'a')
csv_write = csv.writer(out,dialect='excel')
stu = ['No','song name','singer','time']
csv_write.writerow(stu)

for file in os.listdir(PATH):
	if file in ['.DS_Store']:
		pass
	else:
		path = PATH+'/'+file
		try:
			audio = mediainfo(path)
			a = audio['duration']
			a = filter(str.isdigit,a.encode("utf-8"))
			a = int(a[:-6])
			name = os.path.splitext(file)[0]
			singer = ''
			if re.search('.+-.+',name):
				o = re.search('(.+)-(.+)',name)
				name = o.group(1)
				singer = o.group(2)
		except:
			print file,'没有读取时长'
	
	
	
		stu1 = [x,singer,name,datetime.timedelta(seconds=a)]
		x=x+1
		csv_write.writerow(stu1)