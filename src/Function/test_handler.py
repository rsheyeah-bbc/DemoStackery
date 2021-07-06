import unittest
import json
from main import get_location_id, get_weather_forecast

class TestHandler(unittest.TestCase):

    def test_get_location_id(self):
        API_KEY = 'AGbFAKx58hyjQScCXIYrxuEwJh2W2cmv'
        city_name= 'Lerwick,Shetland%20Islands'
        city='Lerwick'
        location_id = get_location_id(API_KEY,city_name,city)
        self.assertEqual(location_id,'2644605')


    def test_get_weather_forecast(self):
        LERWICK = 2644605
        myweather_results_json = get_weather_forecast(LERWICK)
        self.assertTrue(len(myweather_results_json) > 0,"We are creating a new json for Lerwick and it is not null")


if __name__ == '__main__':
    unittest.main()
