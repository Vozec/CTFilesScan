from utils.misc import execmd,b_filesize,System_type
from utils.logger import logger
import os
import os.path

def Get_info(config):
	path = config["path"]
	file = os.path.basename(path)

	## INFO
	if(not config['quiet']):
		logger("[+] Guetting Info...",'info',1,0)

	if(config['system_tp'] == 'linux'):
		line = execmd('xxd -p -l 12 "%s"'%path).decode()
		magic = ' '.join([line[i:i+2] for i in range(0, len(line), 2)]).strip()
		file_cmd = execmd('file "%s"'%path).decode().split(path)[1].split(":")[1].strip()
	
	else:
		line = execmd("powershell -Command \"$bytes = foreach ($b in Get-Content '%s' -Encoding byte -TotalCount 12) {$b.ToString('x2')};Write-Output $bytes \" "%path)
		magic = line.replace(b'\r\n',b' ').decode()
		file_cmd = execmd('bash -c \"file %s\"'%path).decode().split(path)[1].split(":")[1].strip()
	
	size = b_filesize(int(os.path.getsize(path)))	

	if(not config['quiet']):
		logger("[>] File: %s"%file,'warning',0,2,False,False)
		logger("[>] Size: %s"%size,'warning',0,2,False,False)
		logger("[>] Magic Header: %s"%magic,'warning',0,2,False,False)
		logger("[>] File Cmd: %s"%file_cmd,'warning',0,2,False,False)

	return file,file_cmd

def Determine_type(ext_word,config):
	filename,file_res = Get_info(config)
	## Check if ext is in list | Check if "keyworks" are in file_cmd result
	for _ in ext_word:
		for _type in list(_.keys()):
			for ext in list(_[_type]):
				if(filename.endswith(ext) or ext in file_res):
					if(not config['quiet']):
						logger("[+] File Type: %s"%_type,'info',0,0)
					_extension = '.'+filename.split('.')[::-1][0].lower() if '.' in filename else filename
					return _type,_extension

	logger("[-] Extension not supported: %s"%filename,'error',1,0,config['json'])
	exit()

def Modules_listing(modules):
	logger('[+] All Modules:','info',1,0,config['json'])
	logger(f'[*] {"Name" : <17} | {"Linux" : <5} | {"windows" : <5} | {"Extension" : <40}','warning',0,1,config['json'])
	for mod in modules.items():
		cfg = mod[1][1]

		name  	= cfg["name"]
		linux 	= 'True' if cfg["linux"] else 'False'
		windows = 'True' if cfg["windows"] else 'False'
		ext   	= str(list(cfg["type"].items())[0][1])
		logger(f'[>] {name : <17} | {linux : <5} | {windows : <7} | {ext : <40}','warning',0,1,config['json'])