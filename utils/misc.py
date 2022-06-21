import os
import subprocess
import time
import calendar
import random
import binascii

from tempfile import gettempdir
from sys import platform

from utils.logger import logger

def execmd(cmd,t=0.25,debug=False):
    if(debug):
        cnt = subprocess.Popen(cmd,shell=True)
    else:
        cnt = subprocess.Popen(cmd,shell=True,stderr=subprocess.PIPE,stdout=subprocess.PIPE,stdin=subprocess.PIPE)
    for k in range(int(t*240)):
        time.sleep(t)
        if(cnt.poll() is not None):
            try:
                return tuple(x for x in cnt.communicate() if x!=b'')[0]#.decode("")
            except Exception as ex:
                return None
    cnt.kill()
    return None

def b_filesize(l):
	units = ['B','kB','MB','GB','TB','PB']
	for k in range(len(units)):
		if l < (1024**(k+1)):
			break
	return "%4.2f %s" % (round(l/(1024**(k)),2), units[k])

def Random_dir_name(): 
    return str(calendar.timegm(time.gmtime()))+'_'+''.join([random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(8)])

def Create_env(json,path=None):
    try:
        path = (Resolve_tmp() if path==None else path)+Random_dir_name()
        os.mkdir(path)        
        return path
    except Exception as ex:
        logger('[-] Failed to create temporary folder: %s | Error: %s'%(path,ex),'error',0,0,json)

def Resolve_tmp():
    return gettempdir()+'/'

def System_type(json):
    if platform == "linux" or platform == "linux2" or platform == "darwin":
        return 'linux'    
    elif platform == "win32":
        return 'windows'
    else:
        logger('[-] Failed to determine system type (linux/windows)','error',0,0,json)
        exit()

def Convert_Result_2Json(data):
    json_data = '{"result":{%s}}'%(','.join(['"%s": %s'%(d[0],d[1]) for d in data.items()])).replace('\'',"\"")
    return json_data