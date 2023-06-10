import grpc
from concurrent import futures
import time

import meteoServer_pb2
import meteoServer_pb2_grpc


# create a class to define the server functions
class LBService:

    def __init__(self):
        channel1 = 'localhost:50053'
        channel2 = 'localhost:50054'
        channel3 = 'localhost:50055'
        self.channels = [channel1, channel2, channel3]
        self.current_channel = 0



    def add_air_data(self, air_proto):
        channel = self.channels[self.current_channel]
        self.current_channel = (self.current_channel + 1) % len(self.channels)
        newchannel = grpc.insecure_channel(channel)
        stub = meteoServer_pb2_grpc.MeteoServiceStub(newchannel)
        stub.ProcessMeteoData(air_proto)
        print('air collected')
        return 'Done'

    def add_poll_data(self, poll_proto):
        channel = self.channels[self.current_channel]
        self.current_channel = (self.current_channel + 1) % len(self.channels)
        newchannel = grpc.insecure_channel(channel)
        stub = meteoServer_pb2_grpc.MeteoServiceStub(newchannel)
        stub.ProcessPollData(poll_proto)
        print('poll collected')
        return 'Done'


LB_service = LBService()