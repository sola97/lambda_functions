# lambda_adapter.py
from functions.device.device_port import DeviceService
from functions.device.i_device_port import ILambdaAdapterPort
from functions.device.request_data import DeviceFetchParam
from functions.device.request_param_validate_adapter import RequestParamValidateAdapter


class LambdaAdapter(ILambdaAdapterPort):
    def __init__(self, device_adapter, response_converter):
        self.device_service = DeviceService(
            device_adapter=device_adapter,
            response_converter=response_converter
        )

    def handle_request(self, event):
        # 参数验证
        RequestParamValidateAdapter().validate(event)
        param = DeviceFetchParam(oauth_token=event['headers']['OAuth-Token'])
        # 调用服务
        result = self.device_service.fetch_devices_for_user(param)
        return result
