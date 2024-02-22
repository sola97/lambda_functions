from typing import List
import httpx
from common.config import app_configs
from common.logger import logger
from functions.device.device_entity import Device, DevicesResult
from functions.device.i_device_port import IDeviceRepositoryPort


class DeviceAdapter(IDeviceRepositoryPort):
    def __init__(self, client: httpx.Client):
        self.client = client

    def get_devices(self, oauth_token: str) -> List[Device]:
        api_url = app_configs.get('server_url')
        headers = {
            "Authorization": f"Bearer {oauth_token}",
            "Content-Type": "application/json"
        }
        try:
            logger.info(f"请求开始URL: {api_url} with OAuth token")
            response = self.client.post(api_url, headers=headers)
            if response.status_code == 200:
                response_data = response.json()
                return DevicesResult(**response_data).devices
            else:
                logger.error(f"Error fetching devices: {response.status_code}")
                raise Exception(f"Error fetching devices: {response.status_code}")
        except httpx.RequestError as e:
            logger.error(f"An error occurred while fetching devices: {str(e)}")
            raise Exception("An error occurred while fetching devices.")
