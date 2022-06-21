from utils.logger import logger
import os

def Filter_modules(modules,config,ext,_type):
	if(not config['quiet']):
		logger("[+] Filtering modules for a %s file .."%_type,'info',1,0)

	filtered = {}
	for mod in list(modules.items()):
		try:
			config_module = mod[1][1]
			if((config_module['linux'] == True and config['system_tp']=="linux" ) or (config_module['windows'] == True and config['system_tp']=="windows")):
				
				for _ in config_module['type'].items():
					if(config['module'] != None):
						if(config_module['name'].lower() == config['module'].lower() and mod[0] not in filtered.keys()):
							filtered[mod[0]]=mod[1]
							break
					else:
						if(_[0] == _type and (_[1] == [] or ext == os.path.basename(config['path']))):
							filtered[mod[0]]=mod[1]
						elif(ext in _[1]):
							filtered[mod[0]]=mod[1]


		except Exception as ex:
			logger('Error during checking %s module : %s'%(mod[0],ex),'error',0,0,config['json'])
			exit()

	if(not config['quiet']):
		logger('[+] Total Modules Filtered: %s\n'%len(filtered),'info',0,0)

	return filtered