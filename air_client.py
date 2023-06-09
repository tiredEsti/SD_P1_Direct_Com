import grpc
import time

# import the generated classes
import meteoServer_pb2
import meteoServer_pb2_grpc

from meteo_utils import MeteoDataDetector

# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')

# create a stub (client)
stub = meteoServer_pb2_grpc.LBServiceStub(channel)

detector = MeteoDataDetector()

# create a valid request message
air = detector.analyzer_air()
air_proto = LBServer_pb2.RawMeteoData(temperature=air['temperature'], humidity=air['humidity'], timestamp= datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

stub.AddAirData(air_proto)

print("Air data added")

