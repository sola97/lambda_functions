from abc import ABC, abstractmethod
from typing import List

from functions.device.data_models.request_data import DeviceFetchParam
from functions.device.data_models.response_data import DevicesResponse
from functions.device.domain.models import Device


class IDeviceServicePort(ABC):
    @abstractmethod
    def fetch_devices_for_user(self, param: DeviceFetchParam) -> DevicesResponse:
        pass


class IDeviceRepositoryPort(ABC):
    @abstractmethod
    def get_devices(self, user_id: str) -> List[Device]:
        pass


class IDeviceResponseConverterPort(ABC):

    @abstractmethod
    def convert(self, domain_devices: List[Device]) -> DevicesResponse:
        pass


class ILambdaPort(ABC):
    @abstractmethod
    def handle(self, event, context) -> dict:
        pass


class IRequestParamValidatePort(ABC):
    @abstractmethod
    def validate(self, event):
        pass
