#!/bin/bash

while :
do
    python3 air_client.py &
    python3 poll_client.py &
done
