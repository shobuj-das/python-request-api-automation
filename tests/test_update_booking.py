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

    # update_payload = 
    booking_id = 3
    client.request(
        method=HttpMethod.PUT,
        endpoint=f"{EndPoint.UPDATE_BOOKING}/{booking_id}"
    )