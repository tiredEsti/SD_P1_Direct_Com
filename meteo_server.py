import grpc
from concurrent import futures
import time

# import the generated classes
import meteoServer_pb2
import meteoServer_pb2_grpc

# import the original meteo_service.py
from meteo_utils import MeteoDataProcessor
from meteo_service import meteo_service

# create a class to define the server functions
class MeteoServiceServicer(meteoServer_pb2_grpc.MeteoServiceServicer):

    def ProcessMeteoData(self, data, context):
        meteo_service.process_meteo_data(data)
        response = meteoServer_pb2.google_dot_protobuf_dot_empty__pb2.Empty()
        return response

    def ProcessPollData(self, data, context):
        meteo_service.process_pollution_data(data)
        response = meteoServer_pb2.google_dot_protobuf_dot_empty__pb2.Empty()
        return response



# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

meteoServer_pb2_grpc.add_MeteoServiceServicer_to_server(MeteoServiceServicer(),server)

# listen on port 50053, 50054, 50055
print('Starting servers. Listening for meteo or pollution data...')
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
