class BookingAssertion:
    @staticmethod
    def verify_booking_response(response, expected):
        body = response.json()
        booking = body["booking"]

        assert booking["firstname"] == expected["firstname"]
        assert booking["lastname"] == expected["lastname"]
        assert booking["totalprice"] == expected["totalprice"]
        assert booking["depositpaid"] == expected["depositpaid"]

    @staticmethod
    def verify_updated_booking_response(response, expected):
        booking = response.json()

        assert booking["firstname"] == expected["firstname"]
        assert booking["lastname"] == expected["lastname"]
        assert booking["totalprice"] == expected["totalprice"]
        assert booking["depositpaid"] == expected["depositpaid"]
    