from functions.device.adapters.external_api_adapter import ExternalApiDeviceRepositoryAdapter
import json

from functions.device.adapters.response_converter_adapter import DeviceResponseConverterAdapterPort
from functions.device.data_models.request_data import DeviceFetchParam
from functions.device.data_models.response_data import DevicesResponse
from functions.device.domain.services import DeviceService
from functions.device.ports.api_port import ILambdaPort


class LambdaAdapter(ILambdaPort):
    def handle(self, event, context) -> dict:
        user_id: str = event['pathParameters']['user_id']
        param = DeviceFetchParam(user_id=user_id)
        device_repository = ExternalApiDeviceRepositoryAdapter()  # 或通过依赖注入获取
        converter = DeviceResponseConverterAdapterPort()
        service: DeviceService = DeviceService(response_converter=converter, device_repository=device_repository)
        devices: DevicesResponse = service.fetch_devices_for_user(param)
        return {
            'statusCode': 200,
            'body': json.dumps(devices)
        }
