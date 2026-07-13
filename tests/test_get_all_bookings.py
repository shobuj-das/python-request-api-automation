import pytest
from config.end_points import EndPoint
from config.http_methods import HttpMethod

@pytest.mark.smoke
def test_get_all_bookings(client):
    response = client.request(
        method=HttpMethod.GET,
        endpoint=EndPoint.ALL_BOOKINGS
    )

    assert response.status_code == 200
    print(response.json())