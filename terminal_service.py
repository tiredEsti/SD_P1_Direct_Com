import time
from datetime import datetime

import meteoServer_pb2
import meteoServer_pb2_grpc


class TerminalService:

    def __init__(self):
        self.wcoef = []
        self.pcoef = []
        self.wtime = []
        self.ptime = []

    def add_terminal_data(self, data):
        if data.timestampWell != 'None':
            self.wcoef.append(data.well)
            self.wtime.append(datetime.strptime(data.timestampWell, '%Y-%m-%d %H:%M:%S'))
        if data.timestampPoll != 'None':
            self.pcoef.append(data.poll)
            self.ptime.append(datetime.strptime(data.timestampPoll, '%Y-%m-%d %H:%M:%S'))
        return 'Done'
    
    def get_data(self, data):
        if(data == 'well'):
            return self.wcoef
        elif(data == 'poll'):
            return self.pcoef
        elif(data == 'wtime'):
            return self.wtime
        elif(data == 'ptime'):
            return self.ptime

terminal_service = TerminalService()