def help():
	config = {
		'type':{'document':['.py','.txt']},
		'linux':True,
		'windows':True,
		'name':'example_config'
	}
	return config


def scan(config):
	config_current = help()

	## Analysis stuff

	result = "Hello World"

	return result

