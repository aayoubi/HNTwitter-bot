#!/bin/bash

RUNLOG="run.$$.log"
rm -f ${RUNLOG}
count=0
pushd hnbot
./warmup.py >> ${RUNLOG}
while true; do
  echo "running bot: $count"
  ./hnbot.py >> ${RUNLOG}
  let count++
  sleep 600
done
popd
