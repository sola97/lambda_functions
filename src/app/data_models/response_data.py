from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class ServiceStatusResponse:
    serviceName: str
    serviceType: List[str]

@dataclass
class DeviceErrorResponse:
    type: str
    status: str
    detail: str

@dataclass
class DeviceResponse:
    deviceId: str
    serialNumber: str
    model: str
    networkStatus: str
    serviceStatus: List[ServiceStatusResponse] = field(default_factory=list)
    deviceError: Optional[List[DeviceErrorResponse]] = None

@dataclass
class DevicesResponse:
    message: str
    devices: List[DeviceResponse] = field(default_factory=list)