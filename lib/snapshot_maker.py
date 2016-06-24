import requests, json, time

class LibratoSnapshotMaker():

	def __init__(self, duration, user, api_key):
		self.duration = duration
		self.user = user
		self.api_key = api_key

	def make_snapshot(self, chart_id, duration):
		url = "https://metrics-api.librato.com/v1/snapshots?" \
			   "subject[chart][id]={chart_id}&" \
			   "subject[chart][source]=*&" \
			   "subject[chart][type]=stacked&" \
			   "duration={duration}"
		snapshot_response = requests.post(url.format(chart_id = chart_id, duration = duration), auth = (self.user, self.api_key))
		return json.loads(snapshot_response.text)

	def download_snapshot(self, url):
		snapshot_url = None
		while snapshot_url == None:
			snapshots_response = requests.get(url, auth = (self.user, self.api_key))
			response_object = json.loads(snapshots_response.text)
			if response_object['image_href'] != None:
				snapshot_url = response_object['image_href']
			time.sleep(0.5)
		return snapshot_url

	def run(self, chart_id):
		snapshot_url = self.make_snapshot(chart_id, self.duration)['href']
		image_url = self.download_snapshot(snapshot_url)
		return image_url
