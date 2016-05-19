import requests
import os.path
import sys

try:
	account_name = "pawel-1"
	invoice_id = "8927119"

	if os.stat('ix.key').st_size > 0:
		f = open("ix.key","r")
		api_key = f.read()

		r = requests.get("https://"+account_name+".app.invoicexpress.com/invoices/"+invoice_id+".xml?api_key="+api_key)

		print r.text

	else:
		print "Key file is Empty. Exiting"
        sys.exit()

except OSError:
    print "Key file not found. Exiting"
    sys.exit()