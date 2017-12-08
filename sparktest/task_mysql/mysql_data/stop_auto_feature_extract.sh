#!/bin/sh
bot_pids=`ps -ef|grep 'python auto_power_feature_extract'|grep -v grep|awk '{print $2}'`
for bot_pid in $bot_pids; do
	echo $bot_pid
	kill -2 $bot_pid
	sleep 1s
done
