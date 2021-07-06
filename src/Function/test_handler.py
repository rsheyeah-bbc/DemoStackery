import unittest
import json
from main import get_location_id, get_weather_forecast

class TestHandler(unittest.TestCase):

    
    # unit test for get_location_id
    def test_get_location_id(self):
        API_KEY = 'AGbFAKx58hyjQScCXIYrxuEwJh2W2cmv'
        city_name= 'Lerwick,Shetland%20Islands'
        city='Lerwick'
        location_id = get_location_id(API_KEY,city_name,city)
        self.assertEqual(location_id,'2644605')


    # unit test for get_weather_forecast
    def test_get_weather_forecast(self):
        LERWICK = 2644605
        myweather_results_json = get_weather_forecast(LERWICK)
        self.assertTrue(len(myweather_results_json) > 0,"We are creating a new json for Lerwick and it is not null")

        
    # integration test
    def test_intg_get_weather_forecast_for_Lerwick(self):
        API_KEY = 'AGbFAKx58hyjQScCXIYrxuEwJh2W2cmv'
        city_name = 'Lerwick,Shetland%20Islands'
        city = 'Lerwick'
        location_id = get_location_id(API_KEY, city_name, city)
        self.assertEqual(location_id, '2644605')
        LERWICK = 2644605
        myweather_results_json = get_weather_forecast(LERWICK)
        self.assertTrue(len(myweather_results_json) > 0, "We are creating a new json for Lerwick and it is not null")
        t = datetime.datetime.utcnow()
        my_bucket_key = str(t.year)+'/'+str(t.month)+'/'+str(t.day)+'/'+str(t.hour)+'/'+'weather_data'
        BUCKET_NAME = 'lambdastackery-dev-ahussain-bucketres-760527956286'
        s3 = boto3.resource('s3')
        obj = s3.Object(bucket_name=BUCKET_NAME, key=my_bucket_key)
        #print(obj.bucket_name)
        #print(obj.key)
        self.assertEqual(obj.key,my_bucket_key)        

if __name__ == '__main__':
    unittest.main()
