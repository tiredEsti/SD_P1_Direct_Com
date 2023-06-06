import grpc
import datetime
from grpc_tools import routing

# import the generated classes
import meteoServer_pb2
import meteoServer_pb2_grpc

from meteo_utils import MeteoDataDetector

# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')

# create a stub (client)
stub = meteoServer_pb2_grpc.LBStub(channel)

detector = MeteoDataDetector()

# create a valid request message
air = detector.analyzer_air()
air_proto = meteoServer_pb2.RawMeteoData(temperature=air['temperature'], humidity=air['humidity'], timestamp= datetime.now())

stub.AddAirData(air_proto)

#falta pedir grafico