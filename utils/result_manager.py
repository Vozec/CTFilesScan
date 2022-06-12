from utils.logger import logger

def Manage_res(result,config):

	if(config['json']):
		logger(result,'result',0,0,True)
	else:
		for item in result.items():
			logger('[>] %s'%item[0],'flag',0,0,False)
			logger(item[1],'white',0,2,False,False)