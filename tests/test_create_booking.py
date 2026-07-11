import pytest

from config.end_points import EndPoint
from config.http_methods import HttpMethod
from api_client import ApiClient
from utils.json_loader import load_json

client = ApiClient()
booking_data = load_json("testdata/booking/create_booking.json")

@pytest.mark.parametrize("payload", booking_data)
def test_create_booking(payload):

    response = client.request(
        method=HttpMethod.POST,
        endpoint=EndPoint.CREATE_BOOKING,
        payload=payload
    )

    assert response.status_code == 200

    # body = response.json()
    # assert body["booking"]["firstname"] == payload["firstname"]
    # assert body["booking"]["lastname"] == payload["lastname"]
    # assert body["booking"]["totalprice"] == payload["totalprice"]
    # assert body["booking"]["depositpaid"] == payload["depositpaid"]
    # assert body["booking"]["bookingdates"] == payload["bookingdates"]
    # assert body["booking"]["additionalneeds"] == payload["additionalneeds"]

    body = response.json()
    booking = body["booking"]
    assert booking["firstname"] == payload["firstname"]
    assert booking["lastname"] == payload["lastname"]
    assert booking["totalprice"] == payload["totalprice"]
    assert booking["depositpaid"] == payload["depositpaid"]
    assert booking["bookingdates"] == payload["bookingdates"]
    assert booking["additionalneeds"] == payload["additionalneeds"]