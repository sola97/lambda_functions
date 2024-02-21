from injector import Injector
import pytest
from functions.device.request_data import DeviceFetchParam
from .models_test import *

def test_device_service_fetch_devices_for_user(device_service):
    param = DeviceFetchParam(user_id="user_1")
    response = device_service.fetch_devices_for_user(param)
    assert response.message == "Mock response"
    assert len(response.devices) > 0