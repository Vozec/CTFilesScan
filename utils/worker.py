from utils.logger import logger

def Launch_scan(config,modules):
	result = {}
	for mod in list(modules.items()):
		result[mod[0]] = mod[1][0].scan(config)
	return result

## Idea : Thread (max=5) | 
# :( > Unstable + Annoying to do properly all print 
# :) > Faster 