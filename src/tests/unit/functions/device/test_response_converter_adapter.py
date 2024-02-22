import pytest
from functions.device.device_entity import Device, Status, ServiceStatus, Alert
from functions.device.response_converter_adapter import DeviceResponseConverterAdapterPort
from functions.device.response_data import DevicesResponse, DeviceResponse, ServiceStatusResponse, DeviceErrorResponse

test_device_1 = Device(
    id="1",
    name="Device1",
    serial="Serial001",
    model="ModelX",
    status=Status(network_status="online", alert=[Alert(group=1, location=100)]),
    capability=["print"],
    service_status=[ServiceStatus(service_name="ServiceA", service_type=["remote"])]
)

test_device_2 = Device(
    id="2",
    name="Device2",
    serial="Serial002",
    model="ModelY",
    status=Status(network_status="offline"),
    capability=["scan"],
)

expected_devices_response = DevicesResponse(
    message="Devices was successfully retrieved.",
    devices=[
        DeviceResponse(
            deviceId="1",
            serialNumber="Serial001",
            model="ModelX",
            networkStatus="online",
            serviceStatus=[ServiceStatusResponse(serviceName="ServiceA", serviceType=["remote"])],
            deviceError=[DeviceErrorResponse(type="ErrorTypePlaceholder", status="ErrorStatusPlaceholder", detail="ErrorDetailPlaceholder")]
        ),
        DeviceResponse(
            deviceId="2",
            serialNumber="Serial002",
            model="ModelY",
            networkStatus="offline",
            serviceStatus=[],
            deviceError=None
        )
    ]
)

def test_convert_devices_to_devices_response():

    converter = DeviceResponseConverterAdapterPort.DeviceResponseConverterAdapterPort()
    result = converter.convert([test_device_1, test_device_2])
    assert result.message == expected_devices_response.message
    assert len(result.devices) == len(expected_devices_response.devices)
