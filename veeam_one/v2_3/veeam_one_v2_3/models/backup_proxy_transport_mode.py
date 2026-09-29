from enum import Enum


class BackupProxyTransportMode(str, Enum):
    AUTOMATICPROCESSINGMODE = "AutomaticProcessingMode"
    DIRECTSANACCESSPROXY = "DirectSANAccessProxy"
    HOTADDPROXY = "HotAddProxy"
    NETWORKPROXY = "NetworkProxy"
    OFFHOSTPROXY = "OffHostProxy"
    ONHOSTPROXY = "OnHostProxy"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
