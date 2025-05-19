from modules.api.services.get_booking import GetBooking
from modules.api.services.get_booking_ids import GetBookingIds


class BaseTestApi:


    def setup_method(self):
        self.get_booking_ids = GetBookingIds()
        self.get_booking_by_id = GetBooking()