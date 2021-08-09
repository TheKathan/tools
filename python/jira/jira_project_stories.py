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

    url = "https://%s.atlassian.net/rest/api/3/search?jql=project=%s&maxResults=1000" % (config['bitbucket']['Domain'], sys.argv[1])

    auth = HTTPBasicAuth(config['bitbucket']['User'], config['bitbucket']['ApiToken'])

    headers = {
        "Accept": "application/json"
    }

    response = requests.request("GET", url, headers=headers, auth=auth)
    #print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

   
    responseJson = json.loads(response.text)
    issues = responseJson["issues"]
    
    print("==== Project: %s ====\n") % (sys.argv[1])

    for issue in reversed(issues):
        print("%s - %s") % (issue["key"], issue["fields"]["summary"])

    print("\n======================")

