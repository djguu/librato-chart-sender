-How to get the chart's ID's and use them?
For example, this URL
https://metrics.librato.com/s/spaces/606/explore/3419
You will need the last number (3419), and you need to put it on the LibratoChartSender object call as the first parameter inside an array

-Email the people you want?
just write on the LibratoChartSender object call as the second parameter

-If you just want to test the app and check the generated email body, just type "True" (whithout the quotation marks), inside "chart_sender.run()"

-How to change chart duration?
On the run() function at LibratoChartSender() class just change the first parameter "604800" to the time you would like, and you have to put the time in seconds.

-How to change email subject?
Go to the LibratoChartSender class and in the run function change the first parameter ("Librato Weekly Report") to whatever you would like

-How can i change the api key?
You need the have the "<file>.key" on your directory with the respective key 
