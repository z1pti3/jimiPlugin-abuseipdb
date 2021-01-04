from core.models import action
from core import auth, db, helpers

from plugins.abuseipdb.includes import abuseipdb

class _abuseipdbIPInfo(action._action):
    apiToken = str()
    ip = str()
    maxAgeInDays = int()

    def run(self,data,persistentData,actionResult):
        ip = helpers.evalString(self.ip,{"data" : data})
        apiToken = auth.getPasswordFromENC(self.apiToken)
        maxAgeInDays = 30
        if self.maxAgeInDays > 0:
            maxAgeInDays = self.maxAgeInDays

        result = abuseipdb._abuseipdb(apiToken).ipInfo(ip,maxAgeInDays)

        if result:
            actionResult["result"] = True
            actionResult["rc"] = 0
            actionResult["apiResult"] = result
        else:
            actionResult["result"] = False
            actionResult["rc"] = 404
            actionResult["msg"] = "Failed to get a valid response from abuseipdb API"
        return actionResult 

    def setAttribute(self,attr,value,sessionData=None):
        if attr == "apiToken" and not value.startswith("ENC "):
            if db.fieldACLAccess(sessionData,self.acl,attr,accessType="write"):
                self.apiToken = "ENC {0}".format(auth.getENCFromPassword(value))
                return True
            return False
        return super(_abuseipdbIPInfo, self).setAttribute(attr,value,sessionData=sessionData)

class _abuseipdbNetblockInfo(action._action):
    apiToken = str()
    netblock = str()
    maxAgeInDays = int()

    def run(self,data,persistentData,actionResult):
        netblock = helpers.evalString(self.netblock,{"data" : data})
        apiToken = auth.getPasswordFromENC(self.apiToken)
        maxAgeInDays = 30
        if self.maxAgeInDays > 0:
            maxAgeInDays = self.maxAgeInDays

        result = abuseipdb._abuseipdb(apiToken).netblockInfo(netblock,maxAgeInDays)

        if result:
            actionResult["result"] = True
            actionResult["rc"] = 0
            actionResult["apiResult"] = result
        else:
            actionResult["result"] = False
            actionResult["rc"] = 404
            actionResult["msg"] = "Failed to get a valid response from abuseipdb API"
        return actionResult 

    def setAttribute(self,attr,value,sessionData=None):
        if attr == "apiToken" and not value.startswith("ENC "):
            if db.fieldACLAccess(sessionData,self.acl,attr,accessType="write"):
                self.apiToken = "ENC {0}".format(auth.getENCFromPassword(value))
                return True
            return False
        return super(_abuseipdbNetblockInfo, self).setAttribute(attr,value,sessionData=sessionData)

class _abuseipdbGetBlacklist(action._action):
    apiToken = str()
    confidenceMinimum = int()

    def run(self,data,persistentData,actionResult):
        apiToken = auth.getPasswordFromENC(self.apiToken)
        confidenceMinimum = 90
        if self.confidenceMinimum > 0:
            confidenceMinimum = self.confidenceMinimum

        result = abuseipdb._abuseipdb(apiToken).getBlacklist(confidenceMinimum)

        if result:
            actionResult["result"] = True
            actionResult["rc"] = 0
            actionResult["apiResult"] = result
        else:
            actionResult["result"] = False
            actionResult["rc"] = 404
            actionResult["msg"] = "Failed to get a valid response from abuseipdb API"
        return actionResult 

    def setAttribute(self,attr,value,sessionData=None):
        if attr == "apiToken" and not value.startswith("ENC "):
            if db.fieldACLAccess(sessionData,self.acl,attr,accessType="write"):
                self.apiToken = "ENC {0}".format(auth.getENCFromPassword(value))
                return True
            return False
        return super(_abuseipdbGetBlacklist, self).setAttribute(attr,value,sessionData=sessionData)

class _abuseipdbReportIP(action._action):
    apiToken = str()
    ip = str()
    categories = str()
    comment = str()

    def run(self,data,persistentData,actionResult):
        ip = helpers.evalString(self.ip,{"data" : data})
        categories = helpers.evalString(self.categories,{"data" : data})
        comment = helpers.evalString(self.comment,{"data" : data})
        apiToken = auth.getPasswordFromENC(self.apiToken)

        result = abuseipdb._abuseipdb(apiToken).reportIP(ip,categories,comment)

        if result:
            actionResult["result"] = True
            actionResult["rc"] = 0
            actionResult["apiResult"] = result
        else:
            actionResult["result"] = False
            actionResult["rc"] = 404
            actionResult["msg"] = "Failed to get a valid response from abuseipdb API"
        return actionResult 

    def setAttribute(self,attr,value,sessionData=None):
        if attr == "apiToken" and not value.startswith("ENC "):
            if db.fieldACLAccess(sessionData,self.acl,attr,accessType="write"):
                self.apiToken = "ENC {0}".format(auth.getENCFromPassword(value))
                return True
            return False
        return super(_abuseipdbReportIP, self).setAttribute(attr,value,sessionData=sessionData)

class _abuseipdbClearReport(action._action):
    apiToken = str()
    ip = str()

    def run(self,data,persistentData,actionResult):
        ip = helpers.evalString(self.ip,{"data" : data})
        apiToken = auth.getPasswordFromENC(self.apiToken)

        result = abuseipdb._abuseipdb(apiToken).clearReport(ip)

        if result:
            actionResult["result"] = True
            actionResult["rc"] = 0
            actionResult["apiResult"] = result
        else:
            actionResult["result"] = False
            actionResult["rc"] = 404
            actionResult["msg"] = "Failed to get a valid response from abuseipdb API"
        return actionResult 

    def setAttribute(self,attr,value,sessionData=None):
        if attr == "apiToken" and not value.startswith("ENC "):
            if db.fieldACLAccess(sessionData,self.acl,attr,accessType="write"):
                self.apiToken = "ENC {0}".format(auth.getENCFromPassword(value))
                return True
            return False
        return super(_abuseipdbClearReport, self).setAttribute(attr,value,sessionData=sessionData)