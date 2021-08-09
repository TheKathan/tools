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
    fields = responseJson["fields"]
    timeTracking = fields["timetracking"]
    
    
    print("==== Task: %s ====\n") % (sys.argv[1])
    print("%s\n") % (fields["summary"])
    print("Estimate: %d h") % (timeTracking["originalEstimateSeconds"] / 3600)
    print("Time Spent: %d h") % (timeTracking["timeSpentSeconds"] / 3600)
    if (timeTracking["originalEstimateSeconds"] - timeTracking["timeSpentSeconds"]) < 0:
        print("!! Over Estimate: %d h") % ((timeTracking["timeSpentSeconds"] - timeTracking["originalEstimateSeconds"]) / 3600)
    else:
        print("Time Remaining: %d h") % (timeTracking["remainingEstimateSeconds"] / 3600)
    print("\n======================")

