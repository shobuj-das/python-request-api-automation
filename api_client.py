import requests

class ApiClient:
    def get(self, url, headers=None, params=None):
        return requests.get(
            url=url,
            headers=headers,
            params=params
        )
    
    def post(self, url, headers=None, payload=None):
        return requests.post(
            url=url,
            headers=headers,
            json=payload
        )
    
    def put(self, url, headers=None, payload=None):
        return requests.put(
            url=url,
            headers=headers,
            json=payload
        )
    
    def delete(self, url, headers=None):
        return requests.delete(
            url=url,
            headers=headers
        )
