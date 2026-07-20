import pytest
import random

from config.end_points import EndPoint
from config.http_methods import HttpMethod
from utils.json_loader import load_json
from utils.booking_assertion_helper import BookingAssertion

@pytest.mark.smoke
def test_delete_booking(auth_token,client):
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Cookie": f"token={auth_token}"
    }

    id = -1
    while id == -1:
        random_booking_id = random.randint(1,100)
        response = client.request(
            method=HttpMethod.GET,
            endpoint=f"{EndPoint.GET_BOOKING_BY_ID}/{random_booking_id}",
        )
        if response.status_code == 200:
            id = random_booking_id
            break
        
    
    response = client.request(
        method=HttpMethod.DELETE,
        endpoint=f"{EndPoint.DELETE_BOOKING}/{id}",
        headers=headers
    )

    assert response.status_code == 201
