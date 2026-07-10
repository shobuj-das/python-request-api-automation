class EndPoint:
    BASE_URL = 'https://restful-booker.herokuapp.com'

    AUTH = f'{BASE_URL}/auth'
    ALL_BOOKINGS = f'{BASE_URL}/bookings'
    GET_BOOKING_BY_ID = f'{BASE_URL}/booking'
    CREATE_BOOKING = f'{BASE_URL}/booking'
    UPDATE_BOOKING = f'{BASE_URL}/booking'
    PARTIAL_UPDATE = f'{BASE_URL}/booking'
    DELETE_BOOKING = f'{BASE_URL}/booking'