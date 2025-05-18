import pytest

from config import data
from config.base_test_api import BaseTestApi


class TestGetBookingIds(BaseTestApi):

    @pytest.mark.allids
    def test_booking_ids_status_code(self):
        self.get_booking_ids.get_status_code()


    @pytest.mark.allids
    def test_get_booking_ids(self):
        ids = self.get_booking_ids.get_booking_ids()
        assert ids == data.all_ids


    @pytest.mark.allids
    def test_get_id_by_existing_name(self):
        ids = self.get_booking_ids.get_booking_id_by_valid_name(data.valid_first_name)
        assert len(ids) != 0
        assert type(ids[0]) == int


    @pytest.mark.allids
    def test_get_id_by_existing_lastname(self):
        ids = self.get_booking_ids.get_booking_id_by_valid_lastname(data.valid_last_name)
        assert len(ids) != 0
        assert type(ids[0]) == int


    @pytest.mark.allids
    def test_get_id_by_nonexisting_name(self):
        ids = self.get_booking_ids.get_booking_id_by_valid_name(data.non_existing_first_name)
        assert ids == []


    @pytest.mark.allids
    def test_get_id_by_nonexisting_lastname(self):
        ids = self.get_booking_ids.get_booking_id_by_valid_lastname(data.non_existing_last_name)
        assert ids == []