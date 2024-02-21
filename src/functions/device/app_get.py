import json
from functions.device.device_adapter import DeviceAdapter
from functions.device.request_param_validate_adapter import RequestParamValidateAdapter
from functions.device.response_converter_adapter import DeviceResponseConverterAdapterPort
from functions.device.request_data import DeviceFetchParam
from functions.device.response_data import DevicesResponse
from functions.device.device_port import DeviceService

def lambda_handler(event, context):
    try:
        # 参数验证
        RequestParamValidateAdapter().validate(event)
        param = DeviceFetchParam(user_id=event['body']['user_id'])
        # 创建服务实例（可以通过依赖注入框架来实现）
        service = DeviceService(device_repository=DeviceAdapter(),
                                response_converter=DeviceResponseConverterAdapterPort())
        # 调用服务
        result = service.fetch_devices_for_user(param)

        # 构造响应
        return {
            'statusCode': 200,
            'body': json.dumps(result)
        }
    except Exception as e:
        return {'statusCode': 400, 'body': json.dumps({"message": str(e)})}
