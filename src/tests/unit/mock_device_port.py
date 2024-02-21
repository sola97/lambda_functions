from unittest.mock import Mock
from typing import List, Optional
from  functions.device.i_device_port import (IDeviceServicePort, IDeviceRepositoryPort,
                                    IDeviceResponseConverterPort, Device, DevicesResponse)
                                    
class MockDeviceRepositoryPort(IDeviceRepositoryPort):
    def get_devices(self, user_id: str) -> List[Device]:
        return [
            Device(device_id="1", user_id="user_1"),
            Device(device_id="2", user_id="user_2"),
        ]

class MockDeviceResponseConverterPort(IDeviceResponseConverterPort):
    def convert(self, domain_devices: List[Device]) -> DevicesResponse:
        return DevicesResponse(
            message="Mock response",
            devices=domain_devices
        )