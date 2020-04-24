#!/usr/bin/python
# -*- coding:utf-8 -*-

import os, sys, re
import subprocess

path = sys.argv[1]
files = os.listdir(path)


TCfold = path+'/TC'
if not os.path.exists(TCfold):
	os.makedirs(TCfold)

for f in files:
	if f.endswith(('MXF','MP4','MOV')):
		
		file_path = path+'/'+f
		file_data = subprocess.check_output(['ffprobe','-show_streams','-hide_banner',file_path])
		name=file_data.decode('utf8').strip() 
		time_data = re.search('creation_time=.+(\d{2}:\d{2}:\d{2})', name)
		time = time_data.group(1)
		subprocess.call(['ffmpeg','-i',file_path,'-c','copy','-timecode',time+':'+'00',TCfold+'/'+f]) 