import pytest
from unittest.mock import Mock
from functions.device.device_port import DeviceService
from functions.device.i_device_port import IDeviceRepositoryPort, IDeviceResponseConverterPort

from functions.device.request_data import DeviceFetchParam
from functions.device.device_entity import Device
from functions.device.response_data import DevicesResponse, DeviceResponse

# 创建测试用的DeviceFetchParam实例
test_param = DeviceFetchParam(oauth_token="test_oauth_token")

# 创建模拟的Devices列表
mock_devices = [
    Device(id="1", name="Device1", serial="Serial001", model="ModelX", status=None, capability=[], service_status=[]),
    # 可以添加更多的Device实例以进行更全面的测试
]

# 创建预期的DevicesResponse对象
expected_devices_response = DevicesResponse(
    message="Devices was successfully retrieved.",
    devices=[
        DeviceResponse(deviceId="1", serialNumber="Serial001", model="ModelX", networkStatus="unknown", serviceStatus=[], deviceError=None),
        # 根据需要添加更多的DeviceResponse实例
    ]
)


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


def test_fetch_devices_for_user(mock_device_adapter, mock_response_converter):
    # 初始化DeviceService实例，注入模拟的依赖项
    device_service = DeviceService(response_converter=mock_response_converter, device_adapter=mock_device_adapter)

    # 调用fetch_devices_for_user方法
    result = device_service.fetch_devices_for_user(test_param)

    # 验证返回的DevicesResponse是否符合预期
    assert result == expected_devices_response
    # 确认mock_device_adapter.get_devices被正确调用
    mock_device_adapter.get_devices.assert_called_once_with("test_oauth_token")
    # 确认mock_response_converter.convert被正确调用
    mock_response_converter.convert.assert_called_once_with(mock_devices)
