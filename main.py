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

class ApiKeyManager():

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


class LibratoSnapshotMaker():

	def __init__(self, duration, user, apkeyfile):
		self.duration = duration
		self.user = user
		self.apkeyfile = apkeyfile

	def make_snapshot(self, chart_id, duration, user, api_key):
		url = "https://metrics-api.librato.com/v1/snapshots?" \
			   "subject[chart][id]={chart_id}&" \
			   "subject[chart][source]=*&" \
			   "subject[chart][type]=stacked&" \
			   "duration={duration}"
		snapshot_response = requests.post(url.format(chart_id = chart_id, duration = duration), auth = (user, api_key))
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
		api_key = ApiKeyManager().read_api_key(self.apkeyfile)
		snapshot_url = self.make_snapshot(chart_id, self.duration, self.user, api_key)['href']
		image_url = self.download_snapshot(snapshot_url, self.user, api_key)
		return image_url

class HTMLEmailMaker():

	def __init__(self, html_file):
		self.file = html_file

	def insert_snapshots(self, snapshot_urls):
		read_html_file = open(self.file, "r").read()
		template = Template(read_html_file)
		return template.render(charts = snapshot_urls)

class LibratoChartSender():

	TEST_EMAIL_FILE_NAME = "email_template.html"

	def __init__(self, librato_chart_ids, recipients_list):
		self.librato_chart_ids = librato_chart_ids
		self.recipients_list = recipients_list
		self.snapshot_urls = []

	def save_html(self, file_name, code):
		target = open(file_name, "w")
		print "Test email file saved succesfully."
		return target.write(code)

	def send_simple_message(self, subject, email_body, api_key):
	    return requests.post(
        "https://api.mailgun.net/v3/rupeal.com/messages",
        auth = ("api", api_key),
        data = {
			"from": "LibratoChartSender <librato_chart_sender@rupeal.com>",
			"to": self.recipients_list,
			"subject": subject,
			"html": email_body
		})


	def run(self, test_run=False):
		librato_shapshot_maker = LibratoSnapshotMaker("604800", "systems@rupeal.com", "librato.key")
		html_email_maker = HTMLEmailMaker(self.TEST_EMAIL_FILE_NAME)
		api_key = ApiKeyManager().read_api_key('mailgun.key')
		for chart_id in self.librato_chart_ids:
			self.snapshot_urls.append(librato_shapshot_maker.run(chart_id))
		
		email_body = html_email_maker.insert_snapshots(self.snapshot_urls)
		if test_run:
			self.save_html("test_email.html", email_body)
		else:
			self.send_simple_message('Librato Weekly Report', email_body, api_key)
			print "E-mail sent succesfully"
		

chart_sender = LibratoChartSender([3419, 3420], ['goncalo.correia@rupeal.com'])
chart_sender.run()
