import pytest

from config.end_points import EndPoint
from config.http_methods import HttpMethod
from utils.json_loader import load_json
from utils.booking_assertion_helper import BookingAssertion

booking_payloads = load_json("testdata/booking/create_booking.json")

@pytest.mark.parametrize("payload", booking_payloads)
def test_create_booking(client, payload):
    
    response = client.request(
        method=HttpMethod.POST,
        endpoint=EndPoint.CREATE_BOOKING,
        payload=payload
    )

    BookingAssertion.verify_booking_response(response, payload)

    booking_id = response.json()["bookingid"]
    response = client.request(
        method=HttpMethod.GET,
        endpoint= f'{EndPoint.GET_BOOKING_BY_ID}/{booking_id}'
    )

    BookingAssertion.verify_booking_response(response, payload)
    
