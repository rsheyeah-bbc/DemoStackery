
This Function (handler.py) contains the scripts to retrieve the temperature information from the BBC Weather API, transform the results into a JSON  and store it in the s3 bucket every 60 minutes. The unit tests and integration tests are in the test_handler.py file.

For the purposes of the demo and in order to save time, and in the absence of Jenkins, stackery has been used to simulate the deployment process of checking code into github and deploying into AWS. We could have used AWS CodeBuild as well, instead. AWS SAM provides you with a command line tool, the AWS SAM CLI, that makes it easy for you to create and manage serverless applications.

# Dependencies
The solution depends on the availability of the locator service API and weather broker API.

``` #Locator Service 
curl 'https://locator-service.api.bbci.co.uk/locations?api_key=AGbFAKx58hyjQScCXIYrxuEwJh2W2cmv&stack=aws&locale=en&filter=international&place-types=settlement%2Cairport%2Cdistrict&order=importance&s=Lerwick&a=true&format=json' \
  -H 'sec-ch-ua: " Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"' \
  -H 'Referer: https://www.bbc.co.uk/' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36' \
  --compressed 
  ```
  ```
  curl 'https://weather-broker-cdn.api.bbci.co.uk/en/maps/forecasts-observations?locations=2644605' \
  -H 'authority: weather-broker-cdn.api.bbci.co.uk' \
  -H 'sec-ch-ua: " Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36' \
  -H 'accept: */*' \
  -H 'origin: https://www.bbc.co.uk' \
  -H 'sec-fetch-site: cross-site' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-dest: empty' \
  -H 'referer: https://www.bbc.co.uk/' \
  -H 'accept-language: en-US,en;q=0.9,en-GB;q=0.8' \
  -H 'if-none-match: "646e5e1acf37480ac5812d17990bcaa34a4537e5b247968ee93375b4ef0ef4b8"' \
  --compressed
  ```

# Further improvements
The solution can be made re-usable and generic by making use of os parameters. Instead of hard coding the API key, the city name , we can pass them as lambda parameters, through the Environment variables via the cloud formation template, put it in the config dict object and access within the script like
for e.g. os.environ['API_KEY']

# How it works

The cloud formation templates, containing the lambda and s3 components and their respective policies are present in the tempalte.yml file. 
<img width="644" alt="Screenshot 2021-07-06 at 18 41 14" src="https://user-images.githubusercontent.com/16939016/124646818-0c1e4f00-de8d-11eb-8f6b-ec5786cfe856.png">

The Amazon Event Bridge formerly known as Cloud Watch events triggers the lambda function via a scheduled rule , which then processes the script and the results are stored in the S3 bucket. The bucket key is formed as such bucket-name/year/month/date/hour/name_of_file in UTC.

For the purpose of this demo, the schedule is set to run every 5 mins. (It is configurable)

# Results
<img width="1343" alt="Screenshot 2021-07-06 at 19 04 01" src="https://user-images.githubusercontent.com/16939016/124646791-00cb2380-de8d-11eb-808e-c88d023b659f.png">

The format of the json file to store the temperature and location:

```[{"observations": [{"time": "{\"utc\": \"2021-07-06T00:00:00Z\", \"timezone\": \"Europe/London\", \"offset\": \"+01:00\"}", "temperature": "{\"c\": 13, \"f\": 55}"}], "location": "{\"name\": \"Lerwick\", \"container\": \"Shetland Islands\"}"}```

# Monitoring 
As and when the lambda process runs, the events are logged in cloud watch logs.
<img width="1245" alt="Screenshot 2021-07-06 at 19 46 45" src="https://user-images.githubusercontent.com/16939016/124651707-2a874900-de93-11eb-9c83-e7865ccc01e7.png">

