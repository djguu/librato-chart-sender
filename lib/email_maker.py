from jinja2 import Template
class HTMLEmailMaker():

	def __init__(self, html_file):
		self.file = html_file

	def insert_snapshots(self, snapshot_urls):
		read_html_file = open(self.file, "r").read()
		template = Template(read_html_file)
		return template.render(charts = snapshot_urls)