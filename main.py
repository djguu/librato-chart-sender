import requests
from lib.snapshot_maker import LibratoSnapshotMaker
from lib.email_maker import HTMLEmailMaker
from lib.key_manager import ApiKeyManager

class LibratoChartSender():

	TEST_EMAIL_FILE_NAME = "templates/email_template.html"

	def __init__(self, librato_chart_ids, recipients_list, api_keys = { 'librato_api_key': '', 'mailgun_api_key' : '' }):
		self.librato_chart_ids = librato_chart_ids
		self.recipients_list = recipients_list
		self.key_manager = ApiKeyManager()
		self.key_manager.set_keys(api_keys['librato_api_key'], api_keys['mailgun_api_key'])

	def save_html(self, file_name, code):
		target = open(file_name, "w")
		return target.write(code)

	def send_simple_message(self, subject, email_body):
		mailgun_key = self.key_manager.get_key('mailgun')
		return requests.post(
        	"https://api.mailgun.net/v3/rupeal.com/messages",
        	auth = ("api", mailgun_key),
        	data = {
				"from": "LibratoChartSender <librato_chart_sender@rupeal.com>",
				"to": self.recipients_list,
				"subject": subject,
				"html": email_body
			}
		)

	def run(self, test_run=False):
		librato_key = self.key_manager.get_key('librato')
		shapshot_maker = LibratoSnapshotMaker("604800", "systems@rupeal.com", librato_key)
		html_email_maker = HTMLEmailMaker(self.TEST_EMAIL_FILE_NAME)

		snapshot_urls = []
		for chart_id in self.librato_chart_ids:
			snapshot_urls.append(shapshot_maker.run(chart_id))
		
		email_body = html_email_maker.insert_snapshots(snapshot_urls)

		if test_run:
			self.save_html("test_email.html", email_body)
			print "Test email file saved succesfully."
		else:
			self.send_simple_message('Librato Weekly Report', email_body)
			print "E-mail sent succesfully"
		

# chart_sender = LibratoChartSender(
# 	[3419, 3420, 3421],
# 	['pawel.krysiak@rupeal.com'],
# 	{
# 		'librato_api_key' : 'b4bf0341c8cdd3b429826a18d1a07582895fa12c7fb97eb8f2c6bdb015004b86',
# 		'mailgun_api_key' : 'key-a05af654983f6c57ec99904a3b84c7b3'
# 	}
# )
# chart_sender.run()
