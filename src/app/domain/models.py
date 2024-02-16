from dataclasses import dataclass, field
from typing import List, Optional


@dataclass(frozen=True)
class PrinterConfiguration:
    color: List[str]


@dataclass(frozen=True)
class DeviceSpec:
    printer_configuration: PrinterConfiguration


@dataclass(frozen=True)
class Status:
    network_status: str
    device_status: Optional[dict] = None
    alert: Optional[List[dict]] = None


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
    pin_code: Optional[str] = None
    device_spec: Optional[DeviceSpec] = None
    status: Optional[Status] = None
    service_status: List[ServiceStatus] = field(default_factory=list)


@dataclass(frozen=True)
class DevicesResult:
    code: int
    devices: List[Device]
    success: bool
    message: str
