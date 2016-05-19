import urllib2

account_name = "pawel-1"
invoice_id = "8927119"
f = open("ix.key","r")
api_key = f.read()

temp = urllib2.urlopen("https://"+account_name+".app.invoicexpress.com/invoices/"+invoice_id+".xml?api_key="+api_key).read()
print temp
