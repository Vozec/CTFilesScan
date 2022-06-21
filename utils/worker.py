from utils.logger import logger
from utils.traffic_converter import Check_traffic

from os import path
import os

def Launch_scan(config,modules):
	
	if(not path.exists(config['env_dir'])):
		os.mkdir(config['env_dir'])

	if(not config['quiet']):
		logger('[>] Working in directory: %s'%config['env_dir'],'info',0,0)

	if(config['path'].endswith('cap') or config['path'].endswith('pcapng')):
		config['path'] = Check_traffic(config['path'])

	result = {}
	for mod in list(modules.items()):
		try:
			result[mod[1][1]['name']] = mod[1][0].scan(config)
		except Exception as ex:
			if(not config['quiet']):
				logger('[-] Error with "%s" module: %s'%(mod[1][1]['name'],ex),'error',1,0)
	return result

## Idea : Thread (max=5) | 
# :( > Unstable + Annoying to do properly all print 
# :) > Faster 