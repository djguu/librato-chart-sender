## Librato Chart Sender

It's meant to every week send the weekly report charts from librato to the people working at Rupeal

# Usage

### Get the chart's ID's and use them
For example, this URL:
https://metrics.librato.com/s/spaces/606/explore/3419
You will need the last number (3419), and you need to put it on the LibratoChartSender object call as the first parameter inside an array

### Email the people you want
Just write on the LibratoChartSender object call as the second parameter


### Change chart duration
On the run() function at LibratoChartSender() class just change the first parameter "604800" to the time you would like, and you have to put the time in seconds.

### Change email subject
Go to the LibratoChartSender class and in the run function change the first parameter ("Librato Weekly Report") to whatever you would like

### Change the api key
You need the have the "<file>.key" on your directory with the respective key 


If you just want to test the app and check the generated email body, just type "True" (whithout the quotation marks), inside "chart_sender.run()"


