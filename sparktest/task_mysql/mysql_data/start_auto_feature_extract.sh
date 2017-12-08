#!/bin/sh
#sh stop_auto_feature_extract.sh
if [ ! -d "logs" ] ; then
	mkdir logs
fi

nohup python  auto_sfhd_origin_data_extract.py >logs/featureLog 2>&1 &
