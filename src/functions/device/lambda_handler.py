import json
import httpx
from functions.device.device_adapter import DeviceAdapter
from functions.device.lambda_adapter import LambdaAdapter
from functions.device.response_converter_adapter import DeviceResponseConverterAdapterPort


def lambda_handler(event, context):
    try:
        adapter = LambdaAdapter(
            device_adapter=DeviceAdapter(httpx.Client()),
            response_converter=DeviceResponseConverterAdapterPort()
        )
        result = adapter.handle_request(event)

        return {
            'statusCode': 200,
            'body': json.dumps(result)
        }
    except Exception as e:
        return {'statusCode': 400, 'body': json.dumps({"message": str(e)})}