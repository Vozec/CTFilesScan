from utils.misc import execmd
from os import path

def help():
	config = {
		'type':{'picture':['.gif','.jpeg','.jpg','.png','.tiff','.bmp']}, # Prefer to focus on image ext. not all
		'linux':True,
		'windows':False,
		'name':'Stegoveritas'
	}
	return config


def scan(config):
	config_current = help()

	cmd  = "ENV_DIR=%s;"%config['env_dir']
	cmd += "TMP_DIR=$ENV_DIR/stegoVeritas;"
	cmd += "mkdir -p $TMP_DIR;"
	cmd += "stegoveritas %s -out $TMP_DIR -meta -imageTransform -colorMap -trailing;"%config['path']
	cmd += "zip -q -r $TMP_DIR/stegoVeritas.zip $TMP_DIR ;"
	cmd += "mv $TMP_DIR/stegoVeritas.zip $ENV_DIR;"
	cmd += "rm -r $TMP_DIR"

	execmd(cmd)

	result_path = ""
	if(path.exists("%s/stegoVeritas.zip"%config['env_dir'])):
		result_path = "%s/stegoVeritas.zip"%config['env_dir']
	else:
		result_path = " not found .."
	
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