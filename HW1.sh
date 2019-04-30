#!/bin/bash
#206 HW1 - bash script


#use the ping command to test whether a device is online
#results: logged with a timestamp
#run as cron job
#if server is not responding, email the system admin (me)

#create a function that accepts an IP address or hostname as an argument
ping_function(){
	echo "in ping"
	temp="$1"
	echo $temp
	#Parse the output of the ping command
	ping -c3 $temp
	if [ $? -eq 0 ]
	then
		echo "Command Answered"
		echo "$(date)"
		#log $? "Address Answered"
		echo $temp, $(date), "Address Answered" >> /root/HW1log
		#success: 0
	elif [ $? -eq 1 ]
	then
		echo "Not Responding"
		echo "$(date)"
		echo $temp, $(date), "Not Responding" | mail -s "Address not responding" ~/mbox
		#mail < or <<<
		echo $temp, $(date), "Not Responding" >> /root/HW1log
		#no response: 1
	else
		echo "High Latency or Other errors"
		echo "$(date)"
		#high latency - log
		echo $temp, $(date), "High Latency or Other errors" >> /root/HW1log
		#high latency: 2
	fi
}

#check the output status

#If the ping is not responding or is missing packets, report this to the log and send an email
#If the ping is high latency,report this to the log and send an email
#If the ping is normal, report this to the log

ping_function $1
#the script should run every 5 minutes
#done with crontab at call


#to do: use $1, make sure log, mail & cron work

