import requests

from config.settings import BASE_URL

# class ApiClient:
#     def get(self, url, headers=None, params=None):
#         return requests.get(
#             url=url,
#             headers=headers,
#             params=params
#         )
    
#     def post(self, url, headers=None, payload=None):
#         return requests.post(
#             url=url,
#             headers=headers,
#             json=payload
#         )
    
#     def put(self, url, headers=None, payload=None):
#         return requests.put(
#             url=url,
#             headers=headers,
#             json=payload
#         )
    
#     def delete(self, url, headers=None):
#         return requests.delete(
#             url=url,
#             headers=headers
#         )

#(industry practice)
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
            url=endpoint,
            headers=headers,
            json=payload,
            params=params
        )

        return response