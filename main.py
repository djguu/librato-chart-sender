import requests
import os.path
import sys
import json
import urllib3
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import ipdb
import time

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

	def make_snapshot(self, chart_id, duration, user, api_key):
		url = "https://metrics-api.librato.com/v1/snapshots?" \
			   "subject[chart][id]={chart_id}&" \
			   "subject[chart][source]=*&" \
			   "subject[chart][type]=stacked&" \
			   "duration={duration}"
		snapshot_response = requests.post(url.format(chart_id=chart_id, duration=duration), auth = (user, api_key))
		return json.loads(snapshot_response.text)

	def download_snapshot(self, url, user, api_key):
		snapshots_image_response = None
		while snapshots_image_response == None:
			snapshots_image_response_request = requests.get(url, auth = (user, api_key))
			response_object = json.loads(snapshots_image_response_request.text)
			# ipdb.set_trace()
			if response_object['image_href'] != None:
				snapshots_image_response = response_object['image_href']
		
		return snapshots_image_response

	def main(self, chart_id, duration, user, apkeyfile):
		api_key = self.read_api_key(apkeyfile)
		snapshot_url = self.make_snapshot(chart_id, duration, user, api_key)['href']
		image_url = self.download_snapshot(snapshot_url, user, api_key)
		print image_url


LibratoChartSender().main("3419", "604800", "systems@rupeal.com", "librato.key")