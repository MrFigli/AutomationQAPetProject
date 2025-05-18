from modules.api.clients.booking.get_booking_ids import GetBookingIds


class BaseTestApi:


    def setup_method(self):
        self.get_booking_ids = GetBookingIds()