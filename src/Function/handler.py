import json
import requests
import boto3

def handler(event, context):
    main()

    
def get_location_id(API_KEY,city_name,city):
    url = f"https://locator-service.api.bbci.co.uk/locations?api_key={API_KEY}&stack=aws&locale=en&filter=international&place-types=settlement%2Cairport%2Cdistrict&order=importance&s={city_name}&a=true&format=json"
    payload = {}
    headers = {}
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


def get_weather_forecast(location_id):
    url = f"https://weather-broker-cdn.api.bbci.co.uk/en/maps/forecasts-observations?locations={location_id}"
    payload = {}
    headers = {}
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
    print("result",myweather_resutls_json)
    return myweather_resutls_json


def print_to_file(location_forecast_info):
    with open("forecast_data_file.json", "w") as data_file:
        #json.dump(location_forecast_info, data_file, indent=2)
        myweather_forecast = json.dump(location_forecast_info)
        s3 = boto3.client('s3')
        BUCKET_NAME= 'lambdastackery-dev-ahussain-bucketres-760527956286'
        response = s3.put_object(
            Bucket=BUCKET_NAME,
            Key='weather_data',
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
