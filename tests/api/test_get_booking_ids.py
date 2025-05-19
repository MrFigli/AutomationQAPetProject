import pytest
from config import data
from config.base_test_api import BaseTestApi


class TestGetBookingIds(BaseTestApi):

    @pytest.mark.allids
    def test_booking_ids_status_code(self):
        self.get_booking_ids.get_status_code()


    @pytest.mark.allids
    def test_get_booking_ids(self):
        self.get_booking_ids.get_booking_ids()


    @pytest.mark.allids
    def test_get_id_by_existing_name(self):
        self.get_booking_ids.get_booking_id_by_valid_name(data.valid_first_name)


    @pytest.mark.allids
    def test_get_id_by_existing_lastname(self):
        self.get_booking_ids.get_booking_id_by_valid_lastname(data.valid_last_name)


    @pytest.mark.allids
    def test_get_id_by_nonexisting_name(self):
        self.get_booking_ids.get_booking_id_by_invalid_name(data.non_existing_first_name)


    @pytest.mark.allids
    def test_get_id_by_nonexisting_lastname(self):
        self.get_booking_ids.get_booking_id_by_invalid_lastname(data.non_existing_last_name)


    @pytest.mark.allids
    def test_get_id_by_valid_name_invalid_lastname(self):
        self.get_booking_ids.get_booking_id_by_valid_name_invalid_lastname(data.valid_first_name, data.non_existing_last_name)


    @pytest.mark.allids
    def test_get_id_by_invalid_name_valid_lastname(self):
        self.get_booking_ids.get_booking_id_by_inValid_name_valid_lastname(data.non_existing_first_name, data.valid_last_name)


    @pytest.mark.allids
    def test_get_ids_by_checkin_date(self):
        self.get_booking_ids.get_booking_by_checkinDate(data.valid_checkin_date)


    @pytest.mark.allids
    def test_get_ids_by_checkOut_date(self):
        self.get_booking_ids.get_booking_by_checkOutDate(data.valid_checkout_date)


    @pytest.mark.allids
    def test_get_ids_by_invalid_checkin_date(self):
        self.get_booking_ids.get_booking_by_invalid_checkinDate(data.non_existing_date)


    @pytest.mark.allids
    def test_get_ids_by_invalid_dateFormat(self):
        self.get_booking_ids.get_booking_by_invalid_dateFormat(data.invalid_format_date)