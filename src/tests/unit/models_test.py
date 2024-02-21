from injector import Module, Binder, singleton
from injector import Injector
from  functions.device.i_device_port import (IDeviceServicePort, IDeviceRepositoryPort,
                                    IDeviceResponseConverterPort)
from .mock_device_port import MockDeviceRepositoryPort,MockDeviceResponseConverterPort
import pytest

@pytest.fixture
def device_service():
    injector = Injector([DeviceServiceTestModule()])
    return injector.get(IDeviceServicePort)

class DeviceServiceTestModule(Module):
    def configure(self, binder: Binder) -> None:
        binder.bind(IDeviceRepositoryPort, to=MockDeviceRepositoryPort, scope=singleton)
        binder.bind(IDeviceResponseConverterPort, to=MockDeviceResponseConverterPort, scope=singleton)

