import pytest

from config.end_points import EndPoint
from config.http_methods import HttpMethod
from utils.json_loader import load_json
from utils.booking_assertion_helper import BookingAssertion

create_payloads = load_json("testdata/booking/create_booking.json")
update_payloads = load_json("testdata/booking/update_booking_payload.json")

@pytest.mark.sanity
@pytest.mark.parametrize("create_payload, update_payload", zip(create_payloads,update_payloads))
def test_update_booking(
        client,
        auth_token,
        create_payload,
        update_payload
    ):

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Cookie": f"token={auth_token}"
    }

# ---first create a booking
    create_response = client.request(
        method=HttpMethod.POST,
        endpoint=EndPoint.CREATE_BOOKING,
        payload=create_payload
    )

    statusCode = create_response.status_code
    if statusCode == 200:
        BookingAssertion.verify_booking_response(create_response, create_payload)

        bookig_id = create_response.json()["bookingid"]
    # --- update the booking by booking id
        update_response = client.request(
            method=HttpMethod.PUT,
            endpoint=f"{EndPoint.UPDATE_BOOKING}/{bookig_id}",
            payload=update_payload,
            headers=headers
        )
        if update_response.status_code == 200:
            BookingAssertion.verify_updated_booking_response(update_response, update_payload)
        else:
            pytest.fail("Booking Update fail")
    else:
        pytest.fail("Booking Creation Fail")