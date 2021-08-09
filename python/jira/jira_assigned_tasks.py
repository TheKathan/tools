import requests
from requests.auth import HTTPBasicAuth
import json
import sys
import configparser
import datetime

# Arguments order:
# - script name
# - Issue
# - number of Hours
# - comment 

if len(sys.argv) != 2:
    sys.exit("You are missing an argument, you numb skull!")
else:
    config = configparser.ConfigParser()
    config.read('config.ini')

    url = "https://%s.atlassian.net/rest/api/3/issue/%s" % (config['bitbucket']['Domain'], sys.argv[1])

    auth = HTTPBasicAuth(config['bitbucket']['User'], config['bitbucket']['ApiToken'])

    headers = {
    "Accept": "application/json"
    }

    response = requests.request("GET", url, headers=headers, auth=auth)
    #print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

    responseJson = json.loads(response.text)
    timeTracking = responseJson["fields"]["timetracking"]
    
    
    print("==== Task: %s ====\n") % (sys.argv[1])
    print("\nTitle: %s\n") % (sys.argv[1])
    print("Estimate: %d") % (timeTracking["originalEstimateSeconds"] / 3600)
    print("TimeSpent: %d") % (timeTracking["timeSpentSeconds"] / 3600)
    print("TimeRemaining: %d") % (timeTracking["remainingEstimateSeconds"] / 3600)
    print("\n======================")

