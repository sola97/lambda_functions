import json

import pytest
import httpx
from httpx import Response, MockTransport
from unittest.mock import Mock
from common.config import app_configs
from functions.device.device_adapter import DeviceAdapter  # 调整为实际的导入路径
# 模拟成功的API响应
api_response = {
    "code": 200,
    "success": True,
    "message": "Devices retrieved",
    "devices": [
        {
            "id": 1,
            "name": "xxx",
            "serial": "yyyy",
            "model": "xxxx",
            "status": {
                "network_status": "offline"
            },
            "capability": ["print", "scan", "ui"],
            "service_status": []
        },
        {
            "id": 2,
            "name": "xyx",
            "serial": "xyyy",
            "model": "xyx",
            "status": {
                "network_status": "online",
                "device_status": {
                    "print": "idle",
                    "scan": "idle"
                },
                "alert": [
                    {
                        "group": 0,
                        "location": 40000
                    }
                ]
            },
            "capability": ["print", "scan"],
            "service_status": [
                {"service_name": "serviceA", "service_type": ["remote"]},
                {"service_name": "serviceB", "service_type": ["supply", "warranty"]},
                {"service_name": "serviceX", "service_type": ["remote"]}
            ]
        }
    ]
}

@pytest.fixture
def mock_response_success():
    return httpx.Response(status_code=200,
                          content=json.dumps(api_response),
                          headers={"Content-Type": "application/json"})

@pytest.fixture
def mock_response_failure():
    return Response(status_code=400)

# 使用MockTransport来模拟HTTP响应
def mock_api_request(request: httpx.Request) -> httpx.Response:
    # 检查请求的URL或者其他属性，以确定如何响应
    # 例如: if request.url.path == "/some/path":
    return httpx.Response(200, json=api_response)

@pytest.fixture
def device_adapter():
    # 设置MockTransport
    client = httpx.Client(transport=httpx.MockTransport(mock_api_request))
    adapter = DeviceAdapter(client)  # 假设你的Adapter可以接受客户端作为参数
    return adapter

def test_get_devices_success(device_adapter, mock_response_success):
    def mock_request(request):
        return Response(200, json=api_response)  # 假设api_response已经定义

    client = httpx.Client(transport=MockTransport(mock_request))
    device_adapter.client = client  # 假设你可以这样设置DeviceAdapter内部使用的客户端
    devices = device_adapter.get_devices("valid_oauth_token")
    assert len(devices) > 0

def test_get_devices_failure_status_code(device_adapter, mock_response_failure):
    with httpx.Client() as client:
        client.post = Mock(return_value=mock_response_failure)  # 模拟失败的响应
        device_adapter.client = client
        with pytest.raises(Exception):
            device_adapter.get_devices("valid_oauth_token")

def test_get_devices_request_error(device_adapter):
    with httpx.Client() as client:
        device_adapter.client = client
        client.post = Mock(side_effect=httpx.RequestError("Test error"))  # 模拟请求错误
        with pytest.raises(Exception):
            device_adapter.get_devices("valid_oauth_token")
