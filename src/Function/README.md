
This Function contains the scripts to retrieve the temperature information from the BBC Weather API, transform the results into a JSON  and store it in the s3 bucket every 60 minutes.

For the purposes of the demo and in order to save time, and in the absence of Jenkins, stackery has been used to simulate the deployment process of checking code into github and deploying into AWS. We could have used AWS CodeBuild as well, instead. 

# Dependencies
The solution depends on the script hitting the locator service API and weather broker API.

# Further improvements
The solution can be made re-usable and generic by making use of os parameters. Instead of hard coding the API key, the city name , we can pass them as lambda parameters, through the Environment variables via the cloud formation template, put it in the config dict object and access within the script like
for e.g. os.environ['API_KEY']

# How it works

The cloud formation templates, containing the lambda and s3 components and their respective policies are present in the tempalte.yml file. 
<img width="644" alt="Screenshot 2021-07-06 at 18 41 14" src="https://user-images.githubusercontent.com/16939016/124646818-0c1e4f00-de8d-11eb-8f6b-ec5786cfe856.png">


# Results
<img width="1343" alt="Screenshot 2021-07-06 at 19 04 01" src="https://user-images.githubusercontent.com/16939016/124646791-00cb2380-de8d-11eb-808e-c88d023b659f.png">

The format of the json file to store the temperature and location:

```[{"observations": [{"time": "{\"utc\": \"2021-07-06T00:00:00Z\", \"timezone\": \"Europe/London\", \"offset\": \"+01:00\"}", "temperature": "{\"c\": 13, \"f\": 55}"}], "location": "{\"name\": \"Lerwick\", \"container\": \"Shetland Islands\"}"}```
