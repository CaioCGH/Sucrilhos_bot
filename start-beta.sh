#!/bin/bash

echo "let's roll"
now=$(date)
logname="./logs/"$now"_log"
mkdir -p logs
screen -Logfile "${logname}" -L -d -m python3 keep_rolling.py beta-sucribot.py $1
echo "Writing log in ${logname}"

