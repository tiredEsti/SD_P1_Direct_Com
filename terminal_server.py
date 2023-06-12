import grpc
from concurrent import futures
import time

# import the generated classes
import meteoServer_pb2
import meteoServer_pb2_grpc
from terminal_service import terminal_service


# create a class to define the server functions
class TerminalServiceServicer(meteoServer_pb2_grpc.TerminalServiceServicer):

    def AddTerminalData(self, data, context):
        terminal_service.add_terminal_data(data)
        response = meteoServer_pb2.google_dot_protobuf_dot_empty__pb2.Empty()
        return response


# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

meteoServer_pb2_grpc.add_MeteoServiceServicer_to_server(MeteoServiceServicer(),server)

# listen on port 50056
print('Starting server. Listening for terminal data to plot...')
server.add_insecure_port('0.0.0.0:50056')
server.start()

# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
