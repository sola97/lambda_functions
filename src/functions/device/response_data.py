from dataclasses import dataclass
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
    serviceStatus: List[ServiceStatusResponse]
    deviceError: Optional[List[DeviceErrorResponse]]

@dataclass
class DevicesResponse:
    message: str
    devices: List[DeviceResponse]