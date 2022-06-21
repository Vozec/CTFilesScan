from utils.misc import execmd
from os import path
from PIL import Image
import os

def help():
	config = {
		'type':{'picture':['.gif']},
		'linux':True,
		'windows':False,
		'name':'GifFrame'
	}
	return config

def analyseImage(path):
	im = Image.open(path)
	results = {'size': im.size,'mode': 'full',}
	try:
		while True:
			if im.tile:
				tile = im.tile[0]
				update_region = tile[1]
				update_region_dimensions = update_region[2:]
				if update_region_dimensions != im.size:
					results['mode'] = 'partial'
					break
			im.seek(im.tell() + 1)
	except EOFError:
		pass
	return results


def gifextract(path,path_work):
	mode = analyseImage(path)['mode']	
	im = Image.open(path)
	i = 0
	p = im.getpalette()
	last_frame = im.convert('RGBA')	
	try:
		while True:
			if not im.getpalette():
				im.putpalette(p)			
			new_frame = Image.new('RGBA', im.size)
			if mode == 'partial':
				new_frame.paste(last_frame)			
			new_frame.paste(im, (0,0), im.convert('RGBA'))
			new_frame.save(path_work+'%s-%d.png' % (''.join(os.path.basename(path).split('.')[:-1]), i), 'PNG')
			i += 1
			last_frame = new_frame
			im.seek(im.tell() + 1)
	except EOFError:
		return True
	return False

def scan(config):
	config_current = help()

	path1	  = '%s/gifframe.zip'%config['env_dir']
	path_work = '%s/gifpng/'%config['env_dir']
	os.mkdir(path_work)
	cmd = 'zip -q -r %s %s;rm -r %s'%(path1,path_work,path_work)

	gifextract(config['path'],path_work)
	execmd(cmd)
	
	result_path = path1 if path.exists(path1) else ""
	
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