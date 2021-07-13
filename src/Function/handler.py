import requests
import json
import boto3
import datetime
import time

def handler(event, context):
    main()

    
def get_location_id(API_KEY,city_name,city):
    url = f"https://locator-service.api.bbci.co.uk/locations?api_key={API_KEY}&stack=aws&locale=en&filter=international&place-types=settlement%2Cairport%2Cdistrict&order=importance&s={city_name}&a=true&format=json"
    payload = {}
    headers = {}
    try:
        response = requests.request("GET", url, headers=headers, data=payload)
        location_info = response.json()
        location_results = location_info['response']['results']['results']
        location_id = 0
        for loc in location_results:
            if loc["name"] == city:
                location_id= loc["id"]
            else:
                break
        return location_id
    except:
        return location_info

def get_weather_forecast(location_id):
    url = f"https://weather-broker-cdn.api.bbci.co.uk/en/maps/forecasts-observations?locations={location_id}"
    payload = {}
    headers = {}
    try:
        response = requests.request("GET", url, headers=headers, data=payload)
        location_forecast_observations_response = response.json()
        print(f'Weather forecast of location, {location_forecast_observations_response}')
        observations = location_forecast_observations_response['features'][0]['properties']['observations']
        mylocation = location_forecast_observations_response['features'][0]['properties']['location']
        myweather_resutls_json = []
        myweather_obsv = {}
        for obsv in observations:
            myweather_obsv['time'] = json.dumps(obsv["time"])
            myweather_obsv['temperature'] = json.dumps(obsv["temperature"])
            myweather_resutls_json.append({"observations": [{"time":myweather_obsv['time'],"temperature":myweather_obsv['temperature']}],"location":json.dumps(mylocation)})
            time.sleep(1)
        print("result",myweather_resutls_json)
        return myweather_resutls_json
    except:
        return location_forecast_observations_response


def print_to_file(location_forecast_info):
    myweather_forecast = json.dumps(location_forecast_info)
    s3 = boto3.client('s3')
    t = datetime.datetime.utcnow()
    my_bucket_key = str(t.year)+'/'+str(t.month)+'/'+str(t.day)+'/'+str(t.hour)+'/' + 'weather_data'
    BUCKET_NAME= 'lambdastackery-dev-ahussain-bucketres-760527956286'
    response = s3.put_object(
        Bucket=BUCKET_NAME,
        Key=my_bucket_key,
        Body=myweather_forecast,
        ACL='public-read'
    )
    print(response)

    
def main():
    API_KEY = 'AGbFAKx58hyjQScCXIYrxuEwJh2W2cmv'
    my_location_id = get_location_id(API_KEY, 'Lerwick,Shetland%20Islands', 'Lerwick')
    my_location_forecast_info = get_weather_forecast(my_location_id)
    print_to_file(my_location_forecast_info)


if __name__ == '__main__':
    main()
