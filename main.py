import requests
import os.path
import sys
import json
import urllib3
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import ipdb
import time
from jinja2 import Template

class LibratoChartSender():

	def __init__(self, duration, user, apkeyfile):
		self.duration = duration
		self.user = user
		self.apkeyfile = apkeyfile

	def read_api_key(self, fileName):
		if os.path.exists(fileName):
			api_key = open(fileName, "r").read()
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
		snapshot_url = None
		while snapshot_url == None:
			snapshots_response = requests.get(url, auth = (user, api_key))
			response_object = json.loads(snapshots_response.text)
			if response_object['image_href'] != None:
				snapshot_url = response_object['image_href']
			time.sleep(0.5)
		return snapshot_url

	def run(self, chart_id):
		api_key = self.read_api_key(self.apkeyfile)
		snapshot_url = self.make_snapshot(chart_id, self.duration, self.user, api_key)['href']
		image_url = self.download_snapshot(snapshot_url, self.user, api_key)
		return image_url

class HTMLEmailMaker():

	def __init__(self, html_file):
		self.file = html_file

	def insert_snapshots(self, snap1, snap2):
		read_html_file = open(self.file, "r").read()
		template = Template(read_html_file)
		return template.render(chart1 = snap1, chart2 = snap2)



librato_chart = LibratoChartSender("604800", "systems@rupeal.com", "librato.key")
# chart1 = librato_chart.run("3419") # job delay
# chart2 = librato_chart.run("3420") # documents created

html_maker = HTMLEmailMaker("LCSHtml.html"	)
write = html_maker.insert_snapshots(librato_chart.run("3419"), librato_chart.run("3420"))

target = open("teste.html", "w")
target.write(write)