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

if len(sys.argv) != 4:
    sys.exit("You are missing an argument, you numb skull!")
else:
    config = configparser.ConfigParser()
    config.read('config.ini')

    url = "https://%s.atlassian.net/rest/api/3/issue/%s/worklog" % (config['bitbucket']['Domain'], sys.argv[1])

    auth = HTTPBasicAuth(config['bitbucket']['User'], config['bitbucket']['ApiToken'])

    headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
    }

    payload = json.dumps( {
    "timeSpentSeconds": int(sys.argv[2]) * 3600,
    "comment": {
        "type": "doc",
        "version": 1,
        "content": [
        {
            "type": "paragraph",
            "content": [
            {
                "text": sys.argv[3],
                "type": "text"
            }
            ]
        }
        ]
    },
    "started": (datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000+0000"))
    })

    response = requests.request("POST", url, data=payload, headers=headers, auth=auth)

    print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))