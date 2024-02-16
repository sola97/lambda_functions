import httpx
from typing import List
from app.config import app_configs
from app.logger import logger
from app.ports.api_port import IDeviceRepositoryPort
from app.domain.models import Device, DevicesResult

class ExternalApiDeviceRepositoryAdapter(IDeviceRepositoryPort):

    def get_devices(self, user_id: str) -> List[Device]:
        api_url = f"{app_configs.get('server_url')}/apis/v1/users/{user_id}/devices"
        try:
            with httpx.Client() as client:
                logger.info(f"开始请求URL: {api_url}")
                response = client.get(api_url)
                if response.status_code == 200:
                    response_data = response.json()
                    return DevicesResult(**response_data).devices
                else:
                    logger.error(f"Error fetching devices: {response.status_code}")
                    raise Exception(f"Error fetching devices: {response.status_code}")
        except httpx.RequestError as e:
            logger.error(f"An error occurred while fetching devices: {str(e)}")
            raise Exception("An error occurred while fetching devices.")