#!/bin/bash

python3 -m grpc_tools.protoc --proto_path=. --grpc_python_out=. --pyi_out=. --python_out=. ./meteoServer.proto

python3 Lb_server.py
python3 meteo_server.py
python3 terminal_server.py
python3 terminal_server.py

for i in {1..10}
do
    python3 air_client.py
    python3 poll_client.py
    sleep 2
done

python3 proxy.py
