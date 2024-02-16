from app.data_models.request_data import DeviceFetchParam
from app.data_models.response_data import DevicesResponse
from app.ports.api_port import IDeviceServicePort, IDeviceRepositoryPort, IDeviceResponseConverterPort
from app.domain.models import Device
from typing import List


class DeviceService(IDeviceServicePort):
    def __init__(self, response_converter: IDeviceResponseConverterPort, device_repository: IDeviceRepositoryPort):
        self.response_converter = response_converter
        self.device_repository = device_repository

    def fetch_devices_for_user(self, param: DeviceFetchParam) -> DevicesResponse:
        domain_devices = self.device_repository.get_devices(param.user_id)
        return self.response_converter.convert(domain_devices)
