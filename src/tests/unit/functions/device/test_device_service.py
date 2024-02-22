import pytest
from unittest.mock import Mock
from functions.device.device_service import DeviceService
from functions.device.i_device_port import IDeviceRepositoryPort, IDeviceResponseConverterPort

from functions.device.request_data import DeviceFetchParam
from functions.device.device_entity import Device
from functions.device.response_data import DevicesResponse, DeviceResponse

test_param = DeviceFetchParam(oauth_token="test_oauth_token")

mock_devices = [
    Device(id="1", name="Device1", serial="Serial001", model="ModelX", status=None, capability=[], service_status=[]),
]

expected_devices_response = DevicesResponse(
    message="Devices was successfully retrieved.",
    devices=[
        DeviceResponse(deviceId="1", serialNumber="Serial001", model="ModelX", networkStatus="unknown", serviceStatus=[], deviceError=None),
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
    device_service = DeviceService(response_converter=mock_response_converter, device_adapter=mock_device_adapter)

    result = device_service.fetch_devices_for_user(test_param)

    assert result == expected_devices_response
    mock_device_adapter.get_devices.assert_called_once_with("test_oauth_token")
    mock_response_converter.convert.assert_called_once_with(mock_devices)
