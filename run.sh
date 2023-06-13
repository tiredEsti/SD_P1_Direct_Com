#!/bin/bash

python3 -m grpc_tools.protoc --proto_path=. --grpc_python_out=. --pyi_out=. --python_out=. ./meteoServer.proto

xterm -e "python3 LB_server.py" &
xterm -e "python3 meteo_server.py" &
xterm -e "python3 client1_terminal_server.py" &
xterm -e "python3 client2_terminal_server.py" &


sleep 3

xterm -e "python3 proxy.py" &

sleep 3

for i in {1..50}
do
    python3 air_client.py
    python3 poll_client.py
    sleep 1
done

print("Yo creo que esta de 10")