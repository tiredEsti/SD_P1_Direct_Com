# BEGIN: 8f7a6b1d7c3e
import redis
from datetime import datetime
import time
import grpc

import meteoServer_pb2
import meteoServer_pb2_grpc

# Redis connection
r = redis.Redis(host='localhost', port=6379, db=0)

# Tumbling window size in seconds
Y = 5

# gRPC server connection
channel = grpc.insecure_channel('localhost:50056')
stub = meteoServer_pb2_grpc.TerminalServiceStub(channel)

# Function to calculate mean of coefficients in a list
def calculate_mean(lst):
    return sum(lst) / len(lst)

# Main loop
while True:
    # Get coefficients from Redis list within the tumbling window
    wellc = []
    pollc = []
    wcoeff = r.rpop('meteo')
    pcoeff = r.rpop('poll')
    if wcoeff is None:
        if pcoeff is None:
            time.sleep(Y)
            break

    pollc.append(pcoeff.decode().split(':')[1].strip(')'))
    wellc.append(wcoeff.decode().split(':')[1].strip(')')
    
    timestampwell = wcoeff.decode().split(':')[0].strip('(')
    timestamppoll = pcoeff.decode().split(':')[0].strip('(')
    while True:
        wcoeff = r.rpop('meteo')
        pcoeff = r.rpop('poll')
        if wcoeff is None
            if pcoeff is None:
                break
        
        if wcoeff is not None:
            wellc.append(float(wcoeff.decode().split(':')[1].strip(')')))
        if pcoeff is not None:
            pollc.append(float(pcoeff.decode().split(':')[1].strip(')')))
        

    # Calculate mean of coefficients
    wmean = calculate_mean(wellc)
    pmean = calculate_mean(pollc)
    # Send mean to connected terminals
    response = stub.AddTerminalData(meteoServer_pb2.TerminalData(well = wmean, poll = pmean, timestampWell=timestampwell, timestampPoll=timestamppoll))
    print("Data retrieved from Redis and sent to terminals")
    time.sleep(Y)


