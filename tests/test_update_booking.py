import pytest

from config.end_points import EndPoint
from config.http_methods import HttpMethod
from utils.json_loader import load_json
from utils.booking_assertion_helper import BookingAssertion

def test_update_booking(client, auth_token):
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        "Cookie" : f"token={auth_token}"
    }

    update_payload = load_json("testdata/booking/update_booking_payload.json")
    booking_id = 3
    response = client.request(
        method=HttpMethod.PUT,
        endpoint=f"{EndPoint.UPDATE_BOOKING}/{booking_id}",
        headers=headers,
        payload=update_payload
    )

    BookingAssertion.verify_updated_booking_response(response, update_payload)
    print(response.json())