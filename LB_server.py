import grpc
from concurrent import futures
import time

# import the generated classes
import meteoServer_pb2
import meteoServer_pb2_grpc


from LB_service import LB_service


class LBServiceServicer(meteoServer_pb2_grpc.LBServiceServicer):
 

    def AddAirData(self, air_proto, context):
        LB_service.add_air_data(air_proto)
        response = meteoServer_pb2.google_dot_protobuf_dot_empty__pb2.Empty()
        return response

    def AddPollData(self, poll_proto, context):
        LB_service.add_poll_data(poll_proto)
        response = meteoServer_pb2.google_dot_protobuf_dot_empty__pb2.Empty()
        return response



# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

meteoServer_pb2_grpc.add_LBServiceServicer_to_server(LBServiceServicer(),server)

print('Starting Load Balancer. Listening on port 50051.')
server.add_insecure_port('0.0.0.0:50051')
server.start()

# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
