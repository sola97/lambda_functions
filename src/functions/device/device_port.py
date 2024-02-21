from functions.device.request_data import DeviceFetchParam
from functions.device.response_data import DevicesResponse
from functions.device.i_device_port import IDeviceServicePort, IDeviceRepositoryPort, IDeviceResponseConverterPort


class DeviceService(IDeviceServicePort):
    def __init__(self, response_converter: IDeviceResponseConverterPort, device_adapter: IDeviceRepositoryPort):
        self.response_converter = response_converter
        self.device_adapter = device_adapter

    def fetch_devices_for_user(self, param: DeviceFetchParam) -> DevicesResponse:
        domain_devices = self.device_adapter.get_devices(param.oauth_token)
        return self.response_converter.convert(domain_devices)
