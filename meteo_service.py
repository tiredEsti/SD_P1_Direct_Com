import random

class MeteoService:

    def __init__(self):
        self.meteo_set = set()

    def add_air_data(self, rawmeteodata):
        print('Air data received: ' + rawmeteodata)
        self.meteo_set.add(rawmeteodata)
        return 'Done'
    
    def add_poll_data(self, rawpollutiondata):
        print('Air data received: ' + rawpollutiondata)
        self.meteo_set.add(rawpollutiondata)
        return 'Done'

    def get_data(self):
        return list(self.meteo_set)


meteo_service = MeteoService()
