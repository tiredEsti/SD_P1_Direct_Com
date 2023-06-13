#!/bin/bash

python3 -m grpc_tools.protoc --proto_path=. --grpc_python_out=. --pyi_out=. --python_out=. ./meteoServer.proto

python3 LB_server.py &
python3 meteo_server.py &
python3 terminal_server.py &
python3 terminal_server.py &

sleep 5

while :
do
    python3 air_client.py &
    python3 poll_client.py &
done
python3 proxy.py &

sleep 60

killall python3