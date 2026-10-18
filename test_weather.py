from unittest.mock import Mock
from weather import WeatherService

def test_current_temperature():
    api = Mock()
    api.get_temperature.return_value = 25
    service = WeatherService(api)
    assert service.current_temperature() == 25
