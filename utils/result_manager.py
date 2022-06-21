from utils.logger import logger
from utils.misc import Convert_Result_2Json

def Manage_res(result,config):

	if(config['json']):
		logger(Convert_Result_2Json(result),'result',0,0,False,False)
	else:
		for item in result.items():
			bad = [{"type":"file","path":"","content":""},{"type":"file","path":[],"content":""}]
			if(item[1] not in bad):
				
				logger('[>] %s'%item[0],'flag',1,0,False)
				link = 'path' if item[1]['type']=="file" else 'content'

				if(type(item[1][link]) == str):
					logger(''.join(['Result at: ' if link == "path" else ""] )+item[1][link],'white',0,2,False,False)
				else:
					for elem in item[1][link]:
						logger(''.join(['Result at: ' if link =="path" else "" ])+elem,'white',0,2,False,False)