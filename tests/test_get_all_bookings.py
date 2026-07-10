
from end_points import EndPoint
from api_client import ApiClient
from config.http_methods import HttpMethod

client = ApiClient()

def test_get_all_bookings(self, url):
    response = client.request(
        method= HttpMethod.GET,
        endpoint=EndPoint.ALL_BOOKINGS
    )

    assert response.status_code == 200
    print(response.json())
