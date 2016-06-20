import os, sys
class ApiKeyManager():

	def read_api_key(self, file_name):
		if os.path.exists(file_name):
			api_key = open(file_name, "r").read()
			if(len(api_key) != 0):
				return api_key
			else:
				return "{file_name} key file is empty. Exiting".format(file_name=file_name)
				sys.exit()
		else:
			print "{file_name} file not found. Exiting".format(file_name=file_name)
	    	sys.exit()