import pytest
from config import data
from config.base_test_api import BaseTestApi


class TestGetBooking(BaseTestApi):


    @pytest.mark.bookingbyid
    def test_get_booking_by_id_status_code(self):
        self.get_booking_by_id.get_status_code()


    @pytest.mark.bookingbyid
    def test_get_booking_by_id(self):
        self.get_booking_by_id.get_valid_booking(data.valid_id)


    @pytest.mark.bookingbyid
    def test_get_booking_by_inValid_id(self):
        self.get_booking_by_id.get_inValid_booking(data.invalid_id)