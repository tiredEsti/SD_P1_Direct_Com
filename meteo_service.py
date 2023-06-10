import redis

import meteoServer_pb2
import meteoServer_pb2_grpc

from meteo_utils import MeteoDataProcessor
connection = redis.Redis(host='localhost', port=6379, db=0)
class MeteoService:

    def __init__(self):
        self.meteo_set = set()

    def process_meteo_data(self, data):
        processor = MeteoDataProcessor()
        coef = processor.process_meteo_data(data)
        connection.rpush('meteo', f'({data.timestamp} : {coef})') 
        print('Wellness data received and stored')
        return 'Done'
    
    def process_pollution_data(self, data):
        processor = MeteoDataProcessor()
        coef = processor.process_pollution_data(data)
        connection.rpush('poll', f'({data.timestamp} : {coef})')
        print('Pollution data received and stored')
        return 'Done'

meteo_service = MeteoService()
