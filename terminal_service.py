import redis

import meteoServer_pb2
import meteoServer_pb2_grpc


class TerminalService:

    def __init__(self):
        self.plot = []
        
    def add_terminal_data(self, data):
        return 'Done'


terminal_service = TerminalService()