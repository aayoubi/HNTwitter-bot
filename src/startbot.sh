#!/bin/bash

RUNLOG="run.$$.log"
rm -f ${RUNLOG}
count=0
./warmup.py >> ${RUNLOG}
while true; do
  echo "running bot: $count"
  ./twitterbot.py >> ${RUNLOG}
  let count++
  sleep 600
done


