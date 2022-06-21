from utils.misc import execmd
from os import path

import numpy
import matplotlib.pyplot as plt
from PIL import Image

def help():
	config = {
		'type':{'picture':['.png']},
		'linux':True,
		'windows':False,
		'name':'LsbGraph'
	}
	return config

def lsb_graph(in_file,savepath):
	BS = 100
	img = Image.open(in_file)
	(width, height) = img.size
	conv = img.convert("RGBA").getdata()
	vr = []
	vg = []
	vb = []
	for h in range(height):
		for w in range(width):
			(r, g, b, a) = conv.getpixel((w, h))
			vr.append(r & 1)
			vg.append(g & 1)
			vb.append(b & 1)
	avgR = []
	avgG = []
	avgB = []
	for i in range(0, len(vr), BS):
		avgR.append(numpy.mean(vr[i:i + BS]))
		avgG.append(numpy.mean(vg[i:i + BS]))
		avgB.append(numpy.mean(vb[i:i + BS]))
	numBlocks = len(avgR)
	blocks = [i for i in range(0, numBlocks)]
	plt.axis([0, len(avgR), 0, 1])
	plt.ylabel('Average LSB per block')
	plt.xlabel('Block number')
	plt.plot(blocks, avgB, 'bo')
	plt.savefig(savepath)

def scan(config):
	config_current = help()

	path1 = '%s/lsbgraph.png'%config['env_dir']
	lsb_graph(config['path'],path1)
	
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