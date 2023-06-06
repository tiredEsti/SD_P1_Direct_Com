import grpc
from concurrent import futures
import time

# import the generated classes
import meteoServer_pb2
import meteoServer_pb2_grpc

channels = ['Channel 1', 'Channel 2', 'Channel 3']
current_channel = 0


# create a class to define the server functions
class LB(meteoServer_pb2_grpc.LBServicer):
    
        channel1 = grpc.insecure_channel('localhost:50053')
        channel2 = grpc.insecure_channel('localhost:50054')
        channel3 = grpc.insecure_channel('localhost:50055')
        channels[] = [channel1, channel2, channel3]
    
    

    def AddAirData(self, air_proto, context):
        channel = channels[current_channel]
        current_channel = (current_channel + 1) % len(channels)

        newchannel = grpc.insecure_channel(channel)
        stub = meteoServer_pb2_grpc.MeteoServiceStub(channel)
        stub.AddAirData(air_proto)
        
        response = meteoServer_pb2.google_dot_protobuf_dot_empty__pb2.Empty()
        return response

    def AddPollData(self, poll_proto, context):
        channel = channels[current_channel]
        current_channel = (current_channel + 1) % len(channels)

        newchannel = grpc.insecure_channel(channel)
        stub = meteoServer_pb2_grpc.MeteoServiceStub(channel)
        stub.AddAirData(air_proto)
        
        response = meteoServer_pb2.google_dot_protobuf_dot_empty__pb2.Empty()
        return response



# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))

# use the generated function `add_InsultingServiceServicer_to_server`
# to add the defined class to the server
meteoServer_pb2_grpc.add_LBServicer_to_server(
    LBServicer(), server)

# listen on port 50051
print('Starting server. Listening on port 50051.')
server.add_insecure_port('0.0.0.0:50051')
server.start()

# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
