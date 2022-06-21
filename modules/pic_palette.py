#!/usr/bin/env python3

from utils.misc import execmd
from os import path
import shutil
import struct
from binascii import crc32
import os

def help():
	config = {
		'type':{'picture':['.png']},
		'linux':True,
		'windows':False,
		'name':'Palette'
	}
	return config

pngsig = b'\x89PNG\r\n\x1a\n'

def swap_palette(filename, n):
	with open(filename, 'r+b') as f:
		f.seek(0)
		if f.read(len(pngsig)) != pngsig:
			os.system('rm %s'%output)
			return False
		while True:
			chunkstr = f.read(8)
			if len(chunkstr) != 8:
				break
			length, chtype = struct.unpack('>L4s', chunkstr)
			chtype = b'PLTE' if b'PLTE' in chtype else b'IDAT'
			if chtype == b'PLTE':
				curpos = f.tell()
				paldata = f.read(length)
				paldata = (b"\x00\x00\x00" * n) + b"\xff\xff\xff" + (b"\x00\x00\x00" * (256 - n - 1))
				f.seek(curpos)
				f.write(paldata)
				f.write(struct.pack('>L', crc32(chtype+paldata)&0xffffffff))
			else:
				f.seek(length+4, os.SEEK_CUR)

def scan(config):

	config_current = help()

	path1 = '%s/palette_change'%config['env_dir']
	path_save = '%s/palette_change.zip'%config['env_dir']

	if not path.exists(path1):
		os.mkdir(path1)

	for i in range(0,255):
		output = "%s/change_%s.png"%(path1,i)
		shutil.copyfile(config['path'], output)
		swap_palette(output,i)

	cmd = 'zip -q -r %s/palette_change.zip %s ;rm -r %s'%(config['env_dir'],path1,path1)
	execmd(cmd)
	
	result_path = path_save if path.exists(path_save) else ""
	
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