#!/usr/bin/python
# -*- coding:utf-8 -*-
''' 
RULES:
Variable all caps
Capitalize the first letter of the function

update：
添加备注项，命名可以兼容4段式和5段式命名。
例：	0421_5D_hxm_01_01
    0421_5D_02_01
    
防止单卡内部重名的素材被覆盖掉。
机位号支持3位数，卡号支持大小写英文

'''

import os, sys, re,time
import subprocess

PATH = sys.argv[1]
#============1========|====2===|=====3=======|=====4====|===5====6======|====|===================7===============|===
RE = '(.+/01_Original/)(\d{4})/([a-zA-Z0-9]+)/*([a-zA-Z]*)/([0-9]+)_([0-9a-zA-z]+)/*.*/([a-zA-Z0-9()_.\ ]+.[A-Za-z0-9]{3})$'

def Go(PATH):
	if '01_Original' in PATH:	
		for root,dirs,files in os.walk(PATH):
			Sort(root,files)
	else:
		print """
		没有在01_Original目录下运行。请注意大小写和数字位数!"""
		print PATH,"is False"



def Sort(root,files):
	
	if re.search('AVCHD$',root):
		if float(get_dir_size(root)) > int(0.2):
			#==============|=1==|==2==|======3========|====4=====|===5=========6===|===|==7====|
			o = re.search('(.+/)(\d{4})/([a-zA-Z0-9]+)/*([a-zA-Z]*)/([0-9]+)_([0-9a-zA-z]+)/*.*/(AVCHD)$',root)
			try:
				if o.group(4):
					CARD = o.group(2)+'_'+o.group(3)+'_'+o.group(4)+'_'+o.group(5).zfill(2)+'_'+o.group(6).zfill(2)
				else:
					CARD = o.group(2)+'_'+o.group(3)+'_'+o.group(5).zfill(2)+'_'+o.group(6).zfill(2)
			except BaseException:
					print '\033[1;31m'+path+'有问题,程序终止'+'\033[0m'
					sys.exit()
			R_PATH = o.group(1).replace('01_Original','02_Rename')+o.group(2)+'/'+o.group(3)+'/'+o.group(4)+'/'+CARD
			T_PATH = o.group(1).replace('01_Original','03_Trans')+o.group(2)+'/'+o.group(3)+'/'+o.group(4)+'/'+CARD
			print '准备提取:   ',CARD,'/',o.group(7)
			Mkdir(R_PATH,T_PATH)
			a= R_PATH+'/'+'AVCHD'
			if os.path.exists(a):
				print '嵌入目录中已有相同文件',a
			else:
				subprocess.call(['mv',root,R_PATH])
				print '\033[1;32m'+'提取成功'+'\033[0m'	

	elif files:
		for F in files:
			path = os.path.join(root,F)
			o = re.search(RE,path)
			if F.endswith(('MXF','MP4','MOV','MTS','mov')):
				try:
					if o.group(4):
						CARD = o.group(2)+'_'+o.group(3)+'_'+o.group(4)+'_'+o.group(5).zfill(2)+'_'+o.group(6).zfill(2)
					else:
						CARD = o.group(2)+'_'+o.group(3)+'_'+o.group(5).zfill(2)+'_'+o.group(6).zfill(2)
				except BaseException:
					print  '\033[1;31m'+path+'有问题,程序终止'+'\033[0m'
					sys.exit()
				R_PATH = o.group(1).replace('01_Original','02_Rename')+o.group(2)+'/'+o.group(3)+'/'+o.group(4)+'/'+CARD
				T_PATH = o.group(1).replace('01_Original','03_Trans')+o.group(2)+'/'+o.group(3)+'/'+o.group(4)+'/'+CARD
				print '准备提取:   ',CARD,'/',o.group(7)
				Mkdir(R_PATH,T_PATH)
				NAME = os.path.basename(path)
				a = R_PATH+'/'+NAME
				b = R_PATH+'/'+CARD+'_'+NAME
				if os.path.exists(a):
					print '嵌入目录中已有相同文件',a
				if os.path.exists(b):
					print '嵌入目录中已有相同文件',b
				else:
					subprocess.call(['mv',path,R_PATH])
					print '\033[1;32m'+'提取成功'+'\033[0m'
					os.rename(R_PATH+'/'+NAME,R_PATH+'/'+CARD+'_'+NAME)
			
			
			if F.endswith(('JPG','PNG','jpg','png')):
				try:
					if o.group(4):
						CARD = o.group(2)+'_'+o.group(3)+'_'+o.group(4)+'_'+o.group(5).zfill(2)+'_'+o.group(6).zfill(2)
					else:
						CARD = o.group(2)+'_'+o.group(3)+'_'+o.group(5).zfill(2)+'_'+o.group(6).zfill(2)
				except BaseException:
					print '\033[1;31m'+path+'有问题,程序终止'+'\033[0m'
					sys.exit()
				R_PATH = o.group(1).replace('01_Original','02_Rename')+o.group(2)+'/'+o.group(3)+'/'+o.group(4)+'/'+CARD+'/Picture'
				T_PATH = o.group(1).replace('01_Original','03_Trans')+o.group(2)+'/'+o.group(3)+'/'+o.group(4)+'/'+CARD
				print '准备提取:   ',CARD,'/',o.group(7)
				Mkdir(R_PATH,T_PATH)
				NAME = os.path.basename(path)
				a = R_PATH+'/'+NAME
				if os.path.exists(a):
					print '嵌入目录中已有相同文件',a
				else:
					subprocess.call(['mv',path,R_PATH])
					print '\033[1;32m'+'提取成功'+'\033[0m'

def Mkdir(R_PATH,T_PATH):
	if not os.path.exists(R_PATH):
		os.makedirs(R_PATH)
	if not os.path.exists(T_PATH):
		os.makedirs(T_PATH)


def get_dir_size(root):
	size = 0
	for root, dirs, files in os.walk(root):
		size += sum([os.path.getsize(os.path.join(root, name)) for name in files])
		sizea = '%.2f' %(size/1000.00/1000.00/1000.00)
	return sizea



if __name__ == '__main__':
	Go(PATH)