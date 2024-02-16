import os
import json
import jsonschema
import yaml
import jsonschema

from functions.device.adapters.external_api_adapter import ExternalApiDeviceRepositoryAdapter
import json

from functions.device.adapters.request_param_validate_adapter import RequestParamValidateAdapter
from functions.device.adapters.response_converter_adapter import DeviceResponseConverterAdapterPort
from functions.device.data_models.request_data import DeviceFetchParam
from functions.device.data_models.response_data import DevicesResponse
from functions.device.domain.services import DeviceService
from functions.device.ports.api_port import ILambdaPort


class LambdaAdapter(ILambdaPort):
    def handle(self, event, context) -> dict:
        try:
            # 参数验证
            RequestParamValidateAdapter().validate(event)
            param = DeviceFetchParam(user_id=event['body']['user_id'])
            # 创建服务实例（可以通过依赖注入框架来实现）
            service: DeviceService = DeviceService(device_repository=ExternalApiDeviceRepositoryAdapter(),
                                                   response_converter=DeviceResponseConverterAdapterPort())
            # 调用服务
            result: DevicesResponse = service.fetch_devices_for_user(param)

            # 构造响应
            return {
                'statusCode': 200,
                'body': json.dumps(result)
            }
        except Exception as e:
            return {'statusCode': 400, 'body': json.dumps({"message": str(e)})}
