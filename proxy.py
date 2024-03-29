import redis
import time
import grpc
from datetime import datetime

import meteoServer_pb2
import meteoServer_pb2_grpc

# Redis connection
r = redis.Redis(host='localhost', port=6379, db=0)

# Tumbling window size in seconds
Y = 5

# gRPC server connection
channel = grpc.insecure_channel('localhost:50056')
channel2 = grpc.insecure_channel('localhost:50057')

stub = meteoServer_pb2_grpc.TerminalServiceStub(channel)
stub2 = meteoServer_pb2_grpc.TerminalServiceStub(channel2)

# Function to calculate mean of coefficients in a list
def calculate_mean(lst):
    return sum(lst) / len(lst)

# Function to get data from Redis return calculate mean and timestamp
def get_data(data):
    coeff = r.rpop(data)
    if coeff is None:
        return [0, 'None']
    ts = coeff.decode().split(" : ")[0].strip('(')
    list = []
    while True:
        value = float(coeff.decode().split(" : ")[1].strip(')'))
        list.append(value)
        coeff = r.rpop(data)
        if coeff is None:
            break
    return [calculate_mean(list), ts]

# Main loop
try:
    while True:   
        time.sleep(Y)
        wdata = get_data('meteo')
        pdata = get_data('poll')
        # Send mean to connected terminals
        #print(type(wdata[1]))
        #print(type(pdata[1]))
        response = stub.AddTerminalData(meteoServer_pb2.ProcessedData(well = wdata[0], poll = pdata[0], timestampWell = wdata[1], timestampPoll = pdata[1]))
        response = stub2.AddTerminalData(meteoServer_pb2.ProcessedData(well = wdata[0], poll = pdata[0], timestampWell = wdata[1], timestampPoll = pdata[1]))
        print("Data retrieved from Redis and sent to terminals")
except KeyboardInterrupt:
    exit(0)

