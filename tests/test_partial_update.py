import pytest

from config.end_points import EndPoint
from config.http_methods import HttpMethod
from utils.json_loader import load_json
from utils.booking_assertion_helper import BookingAssertion

partial_update_payloads = load_json("testdata/booking/partial_update_payloads.json")

@pytest.mark.parametrize("payload", partial_update_payloads)
def test_partial_update(client, auth_token, payload):
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Cookie": f"token={auth_token}"
    }
    id = 6
    response = client.request(
        method=HttpMethod.PATCH,
        endpoint=f'{EndPoint.PARTIAL_UPDATE}/{id}',
        headers=headers,
        payload=payload
    )
    assert response.status_code == 200
    print(response.json())

