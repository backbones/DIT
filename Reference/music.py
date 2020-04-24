#!/usr/bin/python
# -*- coding:UTF-8 -*-

import xml.dom.minidom
import os
import shutil
import sys, commands
import urllib
#
#

xmlpath = sys.argv[1]
out = sys.argv[2]

def xmlread(xmlpath):
	
	dom = xml.dom.minidom.parse(xmlpath)
	root = dom.documentElement
	b = root.getElementsByTagName("pathurl")
	for x in b:
		argv = x.childNodes[0].data
		argv = argv.replace('file://localhost','')
		a = argv.encode('gbk')
		s=urllib.unquote(a)
		
		path =  sys.path[0]
		if s.endswith(('.mp4','.mov', '.jpg', '.png')):
			continue
		else:
			shutil.copyfile(s,out+'/'+os.path.basename(s))
		
if __name__ == "__main__":
	xmlread(xmlpath)