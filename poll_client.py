import grpc
from datetime import datetime

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
poll = detector.analyze_pollution()
currenttime = datetime.now()
poll_proto = meteoServer_pb2.RawPollutionData(co2=poll['co2'], timestamp= currenttime.strftime("%Y-%m-%d %H:%M:%S.%f"))

stub.AddPollData(poll_proto)

print("Pollution data added")

