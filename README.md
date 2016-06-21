## Librato Chart Sender

It's meant to every week send the weekly report charts from librato to the people working at Rupeal

# Version
-version1.0

# Usage

### Get the chart's ID's and use them
For example, this URL:
https://metrics.librato.com/s/spaces/606/explore/3419
You will need the last number (3419), and you need to put it on the LibratoChartSender object call as the first parameter inside an array

###### sample code:
```
chart_sender = LibratoChartSender([3419, 3420], ['goncalo.correia@rupeal.com', 'team-ix@rupeal.com'])

[3419, 3420]-> are the charts we will choose
``` 


### Email the people you want
Just write on the LibratoChartSender object call as the second parameter
###### sample code:
```
chart_sender = LibratoChartSender([3419, 3420], ['team-ix@rupeal.com'])

['team-ix@rupeal.com']-> Are the emails that will receve report
``` 

### Change chart duration
On the run() function at LibratoChartSender() class just change the first parameter "604800" to the time you would like, and you have to put the time in seconds.
###### sample code:
```
LibratoSnapshotMaker("604800", "systems@rupeal.com", "librato.key")

"604800"-> Is the duration of the selected charts
``` 

### Change email subject
Go to the LibratoChartSender class and in the run function change the first parameter ("Librato Weekly Report") to whatever you would like
###### sample code:
```
self.send_simple_message('Librato Weekly Report', email_body, api_key)

'Librato Weekly Report'-> Is the subject of the email
``` 

### Change the api key
Create a folder named keys on the root directory.

You need the have the "<file>.key" on your directory with the respective key
```
'mailgun.key' = file with api key to rupeal mailgun
'librato.key' = file with api key to rupeal librato 
``` 



# Test run option
If you want to test the email before you send something wrong to everybody (including the boss ;)) You should use this option to make sure that your email looks like you think it look.
```
chart_sender = LibratoChartSender([3419, 3420], ['pawel.krysiak@rupeal.com'])
chart_sender.run(True) #-> test run ( produces html file )
chart_sender.run() #-> normal run ( sends an email )
```
