from utils.misc import execmd
from os import path

def help():
	config = {
		'type':{'traffic':['.pcap']},
		'linux':True,
		'windows':False,
		'name':'Tshark'
	}
	return config


def scan(config):
	config_current = help()

	path1 		 = '%s/tshark_metadata.txt'%config['env_dir']
	path2 		 = '%s/tshark_http.txt'%config['env_dir']
	path3 		 = '%s/tshark_dns.txt'%config['env_dir']

	all_path = [path1,path2,path3]

	cmd1 = 'tshark -r %s -q -z http,tree'%(config['path'])
	cmd2 = 'tshark -r %s -Y http.request -T fields -e http.host -e http.user_agent'%(config['path'])
	cmd3 = 'tshark -r %s -T fields -e dns.resp.name'%(config['path'])

	res = [execmd(p).decode() for p in (cmd1,cmd2,cmd3)]

	for i in range(len(all_path)):
		if(res[i].replace('\n','') != 'Running as user "root" and group "root". This could be dangerous.' and res[i].replace('\n','') != ''):
			f = open(all_path[i],'w')
			f.write(res[i].replace('\n\n','\n'))
			f.close()


	result_path = [p for p in all_path if path.exists(p)]

	return {"type":"file","path":result_path,"content":""}




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