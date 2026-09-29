from enum import StrEnum


class AccessTokenRole(StrEnum):
    ADMIN = "Admin"
    BACKUPADMINISTRATOR = "BackupAdministrator"
    CHATBOTADVANCED = "ChatBotAdvanced"
    CHATBOTBASE = "ChatBotBase"
    DASHBOARDVIEWER = "DashboardViewer"
    POWERUSER = "PowerUser"
    READONLYUSER = "ReadonlyUser"
    REPORTCACHINGSERVICE = "ReportCachingService"
    REPORTVIEWER = "ReportViewer"
    SERVICE = "Service"
    TENANT = "Tenant"
    UNKNOWN = "Unknown"
    VBRAPPLICATION = "VbrApplication"
    VDROAPPLICATION = "VdroApplication"
    VDROVSPCAPPLICATION = "VdroVspcApplication"
    VSPCAPPLICATION = "VspcApplication"

    def __str__(self) -> str:
        return str(self.value)
