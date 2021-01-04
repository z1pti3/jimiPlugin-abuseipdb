import requests
import json
import time
from pathlib import Path

class _abuseipdb():
    url = "https://api.abuseipdb.com/api/v2"

    def __init__(self, apiToken, ca=None, requestTimeout=30):
        self.requestTimeout = requestTimeout
        self.apiToken = apiToken
        self.headers = {
            "Key" : "{0}".format(self.apiToken)
        }
        if ca:
            self.ca = Path(ca)
        else:
            self.ca = None

    def apiCall(self,endpoint,methord="GET",data=None):
        kwargs={}
        kwargs["timeout"] = self.requestTimeout
        kwargs["headers"] = self.headers
        if self.ca:
            kwargs["verify"] = self.ca
        try:
            url = "{0}/{1}".format(self.url,endpoint)
            if methord == "GET":
                response = requests.get(url, **kwargs)
            elif methord == "POST":
                kwargs["data"] = data
                response = requests.post(url, **kwargs)
            elif methord == "DELETE":
                response = requests.delete(url, **kwargs)
        except (requests.exceptions.Timeout, requests.exceptions.ConnectionError):
            return 0, "Connection Timeout"
        if response.status_code == 200 or response.status_code == 202:
            return json.loads(response.text)
        return None

    # {'ipAddress': 'x.x.x.x', 'isPublic': True, 'ipVersion': 4, 'isWhitelisted': None, 'abuseConfidenceScore': 0, 'countryCode': 'GB', 'usageType': 'Commercial', 'isp': 'Company Name', 'domain': None, 'hostnames': [], 'totalReports': 0, 'numDistinctUsers': 0, 'lastReportedAt': None}
    def ipInfo(self,ip,maxAgeInDays=30):
        response = self.apiCall("check?ipAddress={0}&maxAgeInDays={1}".format(ip,maxAgeInDays))
        if response:
            return response["data"]
        return response

    # {"networkAddress": "127.0.0.0", "netmask": "255.255.255.0", "minAddress": "127.0.0.1", "maxAddress": "127.0.0.254","numPossibleHosts": 254,"addressSpaceDesc": "Loopback","reportedAddress": [{"ipAddress": "127.0.0.1","numReports": 631,"mostRecentReport": "2019-03-21T16:35:16+00:00","abuseConfidenceScore": 0,"countryCode": null}]}
    def netblockInfo(self,netblock,maxAgeInDays=30):
        response = self.apiCall("check-block?network={0}&maxAgeInDays={1}".format(netblock,maxAgeInDays))
        if response:
            return response["data"]
        return response
        
    # [{'ipAddress': 'x.x.x.x', 'abuseConfidenceScore': 100, 'lastReportedAt': '2021-01-04T19:17:01+00:00'}]
    def getBlacklist(self,confidenceMinimum=90):
        response = self.apiCall("blacklist?confidenceMinimum={0}".format(confidenceMinimum))
        if response:
            return (response["meta"]["generatedAt"], response["data"])
        return response

    # {"ipAddress": "x.x.x.x", "abuseConfidenceScore": 52 }
    def reportIP(self,ip,categories,comment):
        response = self.apiCall("report?ip={0}&categories={1}&comment={2}".format(ip,categories,comment))
        if response:
            return response["data"]
        return response

    # {"numReportsDeleted": 0}
    def clearReport(self,ip):
        response = self.apiCall("clear-address?ip={0}".format(ip))
        if response:
            return response["data"]
        return response
