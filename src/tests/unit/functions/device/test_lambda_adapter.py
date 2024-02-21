from unittest.mock import Mock, patch
import pytest

from functions.device.device_entity import Device
from functions.device.i_device_port import IDeviceRepositoryPort, IDeviceResponseConverterPort
from functions.device.lambda_adapter import LambdaAdapter
from functions.device.request_param_validate_adapter import RequestParamValidateAdapter
from functions.device.device_port import DeviceService
from functions.device.response_data import DeviceResponse, DevicesResponse

# 测试数据
test_event = {
    "headers": {
        "OAuth-Token": "test_token"
    }
}

mock_devices = [
    Device(id="1", name="Device1", serial="Serial001", model="ModelX", status=None, capability=[], service_status=[]),
    # 可以添加更多的Device实例以进行更全面的测试
]

# 创建预期的DevicesResponse对象
expected_devices_response = DevicesResponse(
    message="Devices was successfully retrieved.",
    devices=[
        DeviceResponse(deviceId="1", serialNumber="Serial001", model="ModelX", networkStatus="unknown",
                       serviceStatus=[], deviceError=None),
        # 根据需要添加更多的DeviceResponse实例
    ]
)


@pytest.fixture
def mock_request_param_validate_adapter():
    with patch.object(RequestParamValidateAdapter, 'validate') as mock:
        yield mock


@pytest.fixture
def mock_device_adapter():
    adapter = Mock(spec=IDeviceRepositoryPort)
    adapter.get_devices.return_value = mock_devices
    return adapter


@pytest.fixture
def mock_response_converter():
    converter = Mock(spec=IDeviceResponseConverterPort)
    converter.convert.return_value = expected_devices_response
    return converter


def test_lambda_adapter_handle_request_success(mock_request_param_validate_adapter, mock_device_adapter,
                                               mock_response_converter):
    # 创建 LambdaAdapter 实例
    lambda_adapter = LambdaAdapter(device_adapter=mock_device_adapter, response_converter=mock_response_converter)

    # 调用 handle_request 方法
    result = lambda_adapter.handle_request(test_event)

    # 验证结果
    assert result.message == "Devices was successfully retrieved."
    # 确认 validate 方法被正确调用
    mock_request_param_validate_adapter.assert_called_once()
