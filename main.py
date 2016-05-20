import requests
import os.path
import sys
import librato


class LibratoChartSender():
	def read_api_key(self, fileName):
		if os.path.exists(fileName):
			f = open(fileName, "r")
			api_key = f.read()
			if(len(api_key) != 0):
				return api_key
			else:
				return "Key file is empty. Exiting"
				sys.exit()
		else:
			print "Key file not found. Exiting"
	    	sys.exit()

	def send_request(self, acc_name, iv_id, api_key):
		#r = requests.get("https://" + acc_name + ".app.invoicexpress.com/invoices/" + iv_id + ".xml?api_key=" + api_key)
		r = requests.post("https://metrics-api.librato.com/v1/snapshots?subject[chart][id]=3419&subject[chart][source]=*&subject[chart][type]=stacked&duration=604800", auth=("systems@rupeal.com", "b4bf0341c8cdd3b429826a18d1a07582895fa12c7fb97eb8f2c6bdb015004b86"))
		return r.text

	def main(self, acc_name, iv_id, apkeyfile):
		api_key = self.read_api_key(apkeyfile)
		output = self.send_request(acc_name, iv_id, api_key)
		return output

librato = LibratoChartSender().main("pawel-1", "8927119", "librato.key")
print librato

"""
api = librato.connect("systems@rupeal.com", "b4bf0341c8cdd3b429826a18d1a07582895fa12c7fb97eb8f2c6bdb015004b86")
print api.get_chart(3419, 606)"""