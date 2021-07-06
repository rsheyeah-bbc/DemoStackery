
This Function contains the scripts to retrieve the temperature information from the BBC Weather API, transform the results into a JSON  and store it in the s3 bucket every 60 minutes.

For the purposes of the demo and in order to save time, and in the absence of Jenkins, stackery has been used to simulate the deployment process of checking code into github and deploying into AWS. We could have used AWS CodeBuild as well, instead. The cloud formation templates, containing the lambda and s3 components and their respective policies are present in the tempalte.yml file. As I had constraint on the time, I decided to go with the Stackery Free account.

# Dependencies
The solution depends on hitting the locator service API and weather broker API.

# Further improvements
The solution can be made re-usable and generic by making use of os parameters. Instead of hard coding the API key, the city name , we can pass them as lambda parameters, through the Environment variables via the cloud formation template, put it in the config dict object and access within the script like
for e.g. os.environ['API_KEY']

# How it works


# Results
