class WeatherService:
    def __init__(self, api):
        self.api = api

    def current_temperature(self):
        return self.api.get_temperature()
