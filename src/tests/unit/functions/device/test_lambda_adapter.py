from unittest.mock import Mock, patch
import pytest

from functions.device.device_entity import Device
from functions.device.i_device_port import IDeviceRepositoryPort, IDeviceResponseConverterPort
from functions.device.lambda_adapter import LambdaAdapter
from functions.device.request_param_validate_adapter import RequestParamValidateAdapter
from functions.device.device_service import DeviceService
from functions.device.response_data import DeviceResponse, DevicesResponse

test_event = {
    "headers": {
        "OAuth-Token": "test_token"
    }
}

mock_devices = [
    Device(id="1", name="Device1", serial="Serial001", model="ModelX", status=None, capability=[], service_status=[]),
]


expected_devices_response = DevicesResponse(
    message="Devices was successfully retrieved.",
    devices=[
        DeviceResponse(deviceId="1", serialNumber="Serial001", model="ModelX", networkStatus="unknown",
                       serviceStatus=[], deviceError=None),
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
    lambda_adapter = LambdaAdapter(device_adapter=mock_device_adapter, response_converter=mock_response_converter)

    result = lambda_adapter.handle_request(test_event)

    assert result.message == "Devices was successfully retrieved."
    mock_request_param_validate_adapter.assert_called_once()
