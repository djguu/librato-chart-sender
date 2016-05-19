import requests
import os.path
import sys

class librato_chart_sender():
	def readApiKey(self, fileName):
		if os.path.exists(fileName):
			f = open("ix.key", "r")
			api_key = f.read()
			if(len(api_key) != 0):
				return api_key
			else:
				return "Key file is empty. Exiting"
				sys.exit()
		else:
			print "Key file not found. Exiting"
	    	sys.exit()

	def sendRequest(self, acc_name, iv_id, api_key):
		r = requests.get("https://" + acc_name + ".app.invoicexpress.com/invoices/" + iv_id + ".xml?api_key=" + api_key)
		return r.text

	def main(self, acc_name, iv_id, apkeyfile):
		api_key = self.readApiKey(apkeyfile)
		output = self.sendRequest(acc_name, iv_id, api_key)
		return output


librato = librato_chart_sender().main("pawel-1", "8927119", "ix.key")
print librato