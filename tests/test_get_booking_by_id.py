import pytest
from config.end_points import EndPoint
from config.http_methods import HttpMethod

@pytest.mark.smoke
def test_get_booking_by_id(client):
    booking_id = 3

    response = client.request(
        method=HttpMethod.GET,
        endpoint= f'{EndPoint.GET_BOOKING_BY_ID}/{booking_id}'
    )

    assert response.status_code == 200
    print(response.json())

    