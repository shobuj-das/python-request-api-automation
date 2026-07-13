import requests

from config.settings import BASE_URL
from utils.logger import get_logger

logger = get_logger(__name__)


class ApiClient:

    def request(
        self,
        method,
        endpoint,
        headers=None,
        payload=None,
        params=None
    ):

        url = BASE_URL + endpoint

        # Request Log
        logger.info("=" * 80)
        logger.info(f"REQUEST METHOD : {method}")
        logger.info(f"URL            : {url}")
        logger.info(f"HEADERS        : {headers}")
        logger.info(f"PARAMS         : {params}")
        logger.info(f"PAYLOAD        : {payload}")

        try:
            response = requests.request(
                method=method,
                url=url,
                headers=headers,
                json=payload,
                params=params
        )
        except Exception as e:
            logger.exception(f"Request fail: {e}")

        # Response Log
        logger.info(f"STATUS CODE    : {response.status_code}")
        logger.info(f"RESPONSE BODY  : {response.text}")
        logger.info("=" * 80)

        return response