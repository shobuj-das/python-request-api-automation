import requests

from config.settings import BASE_URL

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

        response = requests.request(
            method=method,
            url=url,
            headers=headers,
            json=payload,
            params=params
        )

        return response