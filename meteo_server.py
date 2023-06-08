import grpc
from concurrent import futures
import time

# import the generated classes
import meteoServer_pb2
import meteoServer_pb2_grpc

# import the original insultingServer.py
from meteo_utils import MeteoDataProcessor


# create a class to define the server functions, derived from
# insultingServer_pb2_grpc.InsultingServiceServicer
class MeteoServiceServicer(meteoServer_pb2_grpc.MeteoServiceServicer):

    def SaveAirData(self, data, context):
        meteo_service.add_insult(insult.value)
        response = insultingServer_pb2.google_dot_protobuf_dot_empty__pb2.Empty()
        return response

    def SavePollData(self, data, context):
        meteo_service.add_insult(insult.value)
        response = insultingServer_pb2.google_dot_protobuf_dot_empty__pb2.Empty()
        return response



# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# use the generated function `add_InsultingServiceServicer_to_server`
# to add the defined class to the server
insultingServer_pb2_grpc.add_InsultingServiceServicer_to_server(
    InsultingServiceServicer(), server)

# listen on port 50051
print('Starting server. Listening for meteo or pollution data...')
server.add_insecure_port('0.0.0.0:50053')
server.add_insecure_port('0.0.0.0:50054')
server.add_insecure_port('0.0.0.0:50055')
server.start()

# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
