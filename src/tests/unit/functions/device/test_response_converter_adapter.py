import pytest
from functions.device.device_entity import Device, Status, ServiceStatus, Alert
from functions.device.response_converter_adapter import DeviceResponseConverterAdapterPort
from functions.device.response_data import DevicesResponse, DeviceResponse, ServiceStatusResponse, DeviceErrorResponse

# 准备测试用的Device实例
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
    # 空的service_status用于测试没有服务状态的情况
)

# 预期的DevicesResponse对象
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
    # 实例化转换器
    converter = DeviceResponseConverterAdapterPort.DeviceResponseConverterAdapterPort()
    # 调用转换方法
    result = converter.convert([test_device_1, test_device_2])
    # 验证结果
    assert result.message == expected_devices_response.message
    assert len(result.devices) == len(expected_devices_response.devices)
    # 更详细的断言可以添加，以验证devices列表中的每个DeviceResponse对象

