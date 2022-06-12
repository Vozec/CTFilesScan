#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# _authors_: Vozec
# _date_ : 08/06/2022

import argparse
import os.path

from utils.importdir import do as LD_modules
from utils.logger import logger
from utils.type_file import Determine_type,Filter_modules
from utils.misc import Create_env,System_type
from utils.worker import Launch_scan
from utils.result_manager import Manage_res

## Pre-Created Extension List
ext_word = [{
	"document":['ASCII text','data'],
	"binary":['ELF'],
	},
	{
	}]

def Header(config):
	if(not config['quiet']):
		logger("  ________ _  _______ __          _____                \n  / ____/ /( )/ ____(_) /__  _____/ ___/_________ _____ \n / /   / __/// /_  / / / _ \\/ ___/\\__ \\/ ___/ __ `/ __ \\\n/ /___/ /_  / __/ / / /  __(__  )___/ / /__/ /_/ / / / /\n\\____/\\__/ /_/   /_/_/\\___/____//____/\\___/\\__,_/_/ /_/ \n                                                        ","progress",0,0,False,False)

def Parse_args():
    parser = argparse.ArgumentParser(add_help=True,description='This tools is used to scan automatically ctf files.')
    parser.add_argument("-f", "--file", dest="file", required=True, help="File paths")
    parser.add_argument("-p", "--password",action="store_true", dest="password",default='password', help="Password")
    parser.add_argument("-i", "--iv", dest="iv",default='30'*16, help="IV in hex")
    parser.add_argument("-m", "--module", dest="module", help="Select a specific module")
    parser.add_argument("-l", "--formatflag", dest="formatflag",default='flag',help="Format Flag (default: 'flag{')")
    parser.add_argument("-j", "--json", dest="json",action="store_true", default=False, help="Use json mode (quit+result formated)")
    parser.add_argument("-o", "--output", dest="output", default=None, help="Select directory to save result")
    return parser.parse_args()

def Setup_config(args):
	config={		
		'env_dir':Create_env(args.json,args.output),
		'system_tp':System_type(args.json),
		'path':args.file.replace('\\','/'),
		'json':args.json,
		'quiet':args.json,
		'password':args.password,
		'iv':args.iv,
		'formatflag':args.formatflag
	}
	if(args.module):config['module']=args.module
	return config


def Load_modules(config):
	modules = LD_modules("./modules/", globals())
	for mod in modules.items():
		try:
			# Add type & extension for each module in final list
			for _ in mod[1][1]['type'].items():
				if(_[0] not in ext_word[1].keys()):ext_word[1][_[0]] = _[1]
				else:
					for ext in _[1]:
						if(ext not in ext_word[1][_[0]]):
							ext_word[1][_[0]].append(ext)
		except Exception as ex:
			logger('Error during loading %s : %s'%(mod[0],ex),'error',0,0,config['json'])
			exit()

	if(not config['quiet']):
		logger('[+] Loading Modules in Memory ..','info',0,0)
		[logger('[>] Module Loaded: %s'%mod,'warning',0,2,False,False) for mod in list(modules.keys())]
		logger('[+] Total Modules in Memory: %s'%len(modules),'info',0,0)

	return modules


def main():
	config 			= Setup_config(Parse_args())
	Header(config)
	modules 		= Load_modules(config)
	_type,extension	= Determine_type(ext_word,config) 
	modules_filtred = Filter_modules(modules,config,extension,_type)
	result 			= Launch_scan(config,modules_filtred)
	Manage_res(result,config)



if __name__ == '__main__':	
	main()