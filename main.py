import requests
import os.path
import sys

def readApiKey(fileName):
	f = open("ix.key","r")
	api_key = f.read()
	return api_key

def sendRequest(acc_name,iv_id,api_key):
	r = requests.get("https://"+acc_name+".app.invoicexpress.com/invoices/"+iv_id+".xml?api_key="+api_key)
	return r.text

account_name = "pawel-1"
invoice_id = "8927119"
ApiKeyFile = "ix.key"

if os.path.exists(ApiKeyFile):
	if os.stat(ApiKeyFile).st_size > 0:
		output = sendRequest(account_name,invoice_id,readApiKey(ApiKeyFile))
		print output
		
	else:
		print "Key file is Empty. Exiting"
       	sys.exit()
else:
    print "Key file not found. Exiting"
    sys.exit()