from core import plugin, model

class _abuseipdb(plugin._plugin):
    version = 0.1

    def install(self):
        # Register models
        model.registerModel("abuseipdbIPInfo","_abuseipdbIPInfo","_action","plugins.abuseipdb.models.action")
        model.registerModel("abuseipdbNetblockInfo","_abuseipdbNetblockInfo","_action","plugins.abuseipdb.models.action")
        model.registerModel("abuseipdbGetBlacklist","_abuseipdbGetBlacklist","_action","plugins.abuseipdb.models.action")
        model.registerModel("abuseipdbReportIP","_abuseipdbReportIP","_action","plugins.abuseipdb.models.action")
        model.registerModel("abuseipdbClearReport","_abuseipdbClearReport","_action","plugins.abuseipdb.models.action")
        return True

    def uninstall(self):
        # deregister models
        model.deregisterModel("abuseipdbIPInfo","_abuseipdbIPInfo","_action","plugins.abuseipdb.models.action")
        model.deregisterModel("abuseipdbNetblockInfo","_abuseipdbNetblockInfo","_action","plugins.abuseipdb.models.action")
        model.deregisterModel("abuseipdbGetBlacklist","_abuseipdbGetBlacklist","_action","plugins.abuseipdb.models.action")
        model.deregisterModel("abuseipdbReportIP","_abuseipdbReportIP","_action","plugins.abuseipdb.models.action")
        model.deregisterModel("abuseipdbClearReport","_abuseipdbClearReport","_action","plugins.abuseipdb.models.action")
        return True

    def upgrade(self,LatestPluginVersion):
        pass
        #if self.version < 0.2:
