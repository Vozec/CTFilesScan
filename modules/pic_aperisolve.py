from utils.misc import execmd
from os import path
import os
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
import json

def help():
	config = {
		'type':{'picture':['.png']},
		'linux':True,
		'windows':True,
		'name':'Aperisolve'
	}
	return config

def aperisolve(img,password='',use_password='false'):
	mp_encoder = MultipartEncoder(
		fields={
	        'file':(os.path.basename(img),open(img, 'rb')),
	        'zsteg_ext':'false',
	        'zsteg_all':'false',
	        'use_password':use_password,
	        'password':password,
	    }
	)
	res = json.loads(requests.post('https://aperisolve.fr/upload',data=mp_encoder,headers={'Content-Type': mp_encoder.content_type}).text)
	if not (res.get('File') is None):
		return 'https://aperisolve.fr/%s'%(str(res["File"]))
	else:
		return 'Error: %s\n'%res["Error"]


def scan(config):
	config_current = help()

	result = [aperisolve(config['path'])]
	if(config['password'] != None):
		result.append(aperisolve(config['path'],config['password'],'true'))

	return {"type":"text","path":"","content":result}

#####################
# "config": 
#####################
# env_dir : Directory Created for the scanned filed
# system_tp : linux/windows
# path : File path
# json : Json response required (optional)
# quiet : Use quiet mode ?  (optional)
# password : Password provided (optional)
# iv : Iv provided (hex) (optional)
# formatflag : Format flag (optional)
# module : Module selected (optional)