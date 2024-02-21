from typing import List
from functions.device.response_data import DevicesResponse, ServiceStatusResponse, DeviceErrorResponse, \
    DeviceResponse
from functions.device.device_entity import Device
from functions.device.i_device_port import IDeviceResponseConverterPort


class DeviceResponseConverterAdapterPort(IDeviceResponseConverterPort):
    class DeviceResponseConverterAdapterPort:
        def convert(self, domain_devices: List[Device]) -> DevicesResponse:
            devices = []
            for device in domain_devices:
                service_status = [
                    ServiceStatusResponse(serviceName=s.service_name, serviceType=s.service_type)
                    for s in device.service_status
                ]

                # Mockup for deviceError, adjust according to your actual data structure
                device_error = []
                if device.status and device.status.alert:
                    # Example transformation, assuming you'll adapt alert details to DeviceErrorResponse
                    for alert in device.status.alert:
                        device_error.append(DeviceErrorResponse(
                            type="ErrorTypePlaceholder",  # Placeholder, adapt as necessary
                            status="ErrorStatusPlaceholder",  # Placeholder, adapt as necessary
                            detail="ErrorDetailPlaceholder"  # Placeholder, adapt as necessary
                        ))

                new_device = DeviceResponse(
                    deviceId=device.id,
                    serialNumber=device.serial,
                    model=device.model,
                    networkStatus=device.status.network_status if device.status else "unknown",
                    serviceStatus=service_status,
                    deviceError=device_error or None
                )
                devices.append(new_device)

            new_response = DevicesResponse(
                message="Devices was successfully retrieved.",
                devices=devices
            )

            return new_response