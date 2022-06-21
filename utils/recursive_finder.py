import os
from utils.logger import logger
from utils.misc import execmd
from os import path
import glob

archive_ext  = ['.bz2','.gz','.bz2','.gz','.tar','.tbz2','.tgz','.zip','.rar','.jar']
foremost_ext = ['.dd','ext4','ext2','ext3','fat32','ntfs','boot sector','DOS/MBR','startsector','.raw']

def Extract(config,zipfile,path):
	cmd = 'extract %s %s'%(zipfile,path)
	if(not config['quiet']):logger('[+] Extracting %s'%zipfile,'info',0,0)
	execmd(cmd)

def Foremost(config,file,folder):
	if(not config['quiet']):logger('[+] Extracting file %s'%file,'info',0,0)
	path_foremost = '%s/foremost'%folder
	cmd = 'foremost %s -o %s'%(file,path_foremost)
	if(path.exists(path_foremost)):
		os.mkdir(path_foremost)
	else:
		execmd('rm -r %s/*'%path_foremost)
	execmd(cmd)

def findall(config,all_files=[],index=0):
	path_extracted = '%s/all_files'%config['env_dir'] 

	if(not path.exists(path_extracted)):
		os.mkdir(path_extracted)
	if(not path.exists(path_extracted+os.path.basename(config['path']))):
		execmd('cp %s %s'%(config['path'],path_extracted))

	files = [f for f in glob.glob("%s/**/*"%path_extracted, recursive=True)]

	for file in files:
		if(file not in all_files):
			file_cmd_res  = execmd('file %s'%file).decode()

			for ext in archive_ext:
				if(file.endswith(ext)):
					Extract(config,file,path_extracted)
					all_files.append(file)
					break


			for ext in foremost_ext:
				if(file.endswith(ext) or ext in file_cmd_res):
					Foremost(config,file,path_extracted)
					all_files.append(file)
					break

			if(file not in all_files):
				all_files.append(file)
			

	files = [f for f in glob.glob("%s/**/*"%path_extracted, recursive=True)]

	max_ = 20
	if len(files) == len(all_files) or index==max_:
		if(index==max_):
			logger('Max Iterations : %s'%max_,'error',0,0,config['json'])
		configs = []
		for file in all_files:
			conf = config.copy()
			conf['path'] = file
			conf['env_dir'] = conf['env_dir'] + '/%s'%os.path.basename(file)
			configs.append(conf)
		return configs
	else:
		index += 1
		return findall(config,all_files,index)

	