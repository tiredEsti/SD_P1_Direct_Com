import grpc
import datetime
from grpc_tools import routing

# import the generated classes
import LB_pb2
import LB_pb2_grpc

from meteo_utils import MeteoDataDetector



# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')

# create a stub (client)
stub = meteoServer_pb2_grpc.LBServiveStub(channel)

detector = MeteoDataDetector()

# create a valid request message
poll = detector.analyzer_pollution()
poll_proto = meteoServer_pb2.RawPolltionData(co2=poll['co2'], timestamp= datetime.now())
stub.AddProtoData(poll_proto)
