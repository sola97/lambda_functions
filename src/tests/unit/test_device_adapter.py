import pytest
import responses
import httpx
from functions.device.device_adapter import DeviceAdapter
from functions.device.device_entity import Device

api_url = "https://example.com/apis/v1/users/user_1/devices"
mock_response_data = {
    "devices": [
        {"device_id": "1", "user_id": "user_1", "device_name": "Device 1"},
        {"device_id": "2", "user_id": "user_1", "device_name": "Device 2"}
    ]
}

@responses.activate
def test_get_devices_success():
    responses.add(responses.GET, api_url, json=mock_response_data, status=200)

    repository = DeviceAdapter()
    devices = repository.get_devices("user_1")

    assert len(devices) == 2
    assert devices[0].device_id == "1"
    assert devices[1].device_id == "2"

@responses.activate
def test_get_devices_failure():
    responses.add(responses.GET, api_url, status=404)

    repository = DeviceAdapter()

    with pytest.raises(Exception) as excinfo:
        repository.get_devices("user_1")
    assert "Error fetching devices" in str(excinfo.value)

@responses.activate
def test_get_devices_http_exception():
    
    responses.add(responses.GET, api_url, body=httpx.RequestError("Error"))

    repository = DeviceAdapter()

    with pytest.raises(Exception) as excinfo:
        repository.get_devices("user_1")
    assert "An error occurred while fetching devices" in str(excinfo.value)
