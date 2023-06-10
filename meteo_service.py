import redis

import meteoServer_pb2
import meteoServer_pb2_grpc

from meteo_utils import MeteoDataProcessor
connection = redis.Redis(host='localhost', port=6379, db=0)
class MeteoService:

    def __init__(self):
        self.meteo_set = set()

    def process_air_data(self, data):
        processor = MeteoDataProcessor()
        coef = processor.process_meteo_data(data)
        bool status = connection.set(data.timestamp : coef, type: 'meteo') 
        if (status)
            print('Wellness data received and stored')
        return 'Done'
    
    def process_poll_data(self, data):
        processor = MeteoDataProcessor()
        coef = processor.process_pollution_data(data)
        bool status = connection.set(data.timestamp : coef, type: 'poll') 
        if (status)
            print('Pollution data received and stored')
        return 'Done'

meteo_service = MeteoService()
