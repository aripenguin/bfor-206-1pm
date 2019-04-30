#!/bin/bash

#homework 1 - bash script
#use the ping command to test whether a device is online
#results: logged with a timestamp
#run as a cron job
#If server is not responding, email the system administrator

#Create a function that accepts an IP address or hostname as an argument
ping_function(){
	echo "in ping"
	let temp=$1
	#Parse the output of the ping command
	let allowedtime == "ping $temp -c3"
	if(allowedtime == 2)
		then echo "Not Responding"
		# not responding - mail 2
	elif(allowedtime == 1)
		then echo "Not Responding"
		#high latency - mail ? 1?
	else
		echo "Command Answered"
		#add address & timestamp 0
	fi
}
#Check the output status

#If the ping is not responding or is missing packets, report this to the log and send an email

#If the ping is high latency, report this to the log and send an email

#If the device is normal, report this to the log

ping_function
#The script should run every 5 minutes
#done with crontab at call
