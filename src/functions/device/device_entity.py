from dataclasses import dataclass, field
from typing import List, Optional, Dict

@dataclass(frozen=True)
class Alert:
    group: int
    location: int

@dataclass(frozen=True)
class Status:
    network_status: str
    device_status: Optional[Dict[str, str]] = None
    alert: Optional[List[Alert]] = None

@dataclass(frozen=True)
class ServiceStatus:
    service_name: str
    service_type: List[str]

@dataclass(frozen=True)
class Device:
    id: str
    name: str
    serial: str
    model: str
    status: Status
    capability: List[str]
    service_status: List[ServiceStatus] = field(default_factory=list)

@dataclass(frozen=True)
class DevicesResult:
    code: int
    success: bool
    message: str
    devices: List[Device]
