import requests
from end_points import EndPoint
from api_client import ApiClient

def test_get_all_bookings(self, url):
    response = ApiClient.get(
        url=url
    )
    print(response)
