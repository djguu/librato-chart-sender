import requests
from lib.snapshot_maker import LibratoSnapshotMaker
from lib.email_maker import HTMLEmailMaker
from lib.key_manager import ApiKeyManager

class LibratoChartSender():

	TEST_EMAIL_FILE_NAME = "templates/email_template.html"

	def __init__(self, librato_chart_ids, recipients_list):
		self.librato_chart_ids = librato_chart_ids
		self.recipients_list = recipients_list
		self.snapshot_urls = []

	def save_html(self, file_name, code):
		target = open(file_name, "w")
		return target.write(code)

	def send_simple_message(self, subject, email_body):
		api_key = ApiKeyManager().read_api_key('keys/mailgun.key')
		return requests.post(
        	"https://api.mailgun.net/v3/rupeal.com/messages",
        	auth = ("api", api_key),
        	data = {
				"from": "LibratoChartSender <librato_chart_sender@rupeal.com>",
				"to": self.recipients_list,
				"subject": subject,
				"html": email_body
			}
		)

	def run(self, test_run=False):
		librato_shapshot_maker = LibratoSnapshotMaker("604800", "systems@rupeal.com", "keys/librato.key")
		html_email_maker = HTMLEmailMaker(self.TEST_EMAIL_FILE_NAME)

		for chart_id in self.librato_chart_ids:
			self.snapshot_urls.append(librato_shapshot_maker.run(chart_id))
		
		email_body = html_email_maker.insert_snapshots(self.snapshot_urls)

		if test_run:
			self.save_html("test_email.html", email_body)
			print "Test email file saved succesfully."
		else:
			self.send_simple_message('Librato Weekly Report', email_body)
			print "E-mail sent succesfully"
		

chart_sender = LibratoChartSender([3419, 3420, 3421], ['pawel.krysiak@rupeal.com'])
chart_sender.run()
