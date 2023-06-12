import redis
import time
import grpc

import meteoServer_pb2
import meteoServer_pb2_grpc

# Redis connection
r = redis.Redis(host='localhost', port=6379, db=0)

# Tumbling window size in seconds
Y = 10

# gRPC server connection
channel = grpc.insecure_channel('localhost:50056')
stub = meteoServer_pb2_grpc.TerminalServiceStub(channel)

# Function to calculate mean of coefficients in a list
def calculate_mean(lst):
    return sum(lst) / len(lst)

# Function to get data from Redis return calculate mean and timestamp
def get_data(type):
    coeff = r.rpop(type)
    if coeff is None:
        return [None, None]
    timestamp = coeff.decode().split(':')[0].strip('(')
    while True:
        value = float(coeff.decode().split(':')[1].strip(')'))
        list.append(value)
        coeff = r.rpop(type)
        if coeff is None:
            break
    return [calculate_mean(list), timestamp]

# Main loop
while True:   
    wdata = get_data('meteo')
    pdata = get_data('poll')
    # Send mean to connected terminals
    response = stub.AddTerminalData(meteoServer_pb2.TerminalData(well = wdata[0], poll = pdata[0], timestampWell = wdata[1], timestampPoll = pdata[1]))
    print("Data retrieved from Redis and sent to terminals")
    time.sleep(Y)


