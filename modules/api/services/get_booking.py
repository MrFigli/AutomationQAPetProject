import requests
from config import data
from modules.api.services.endpoints import Endpoints


class GetBooking:


    def __init__(self):
        self.endpoints = Endpoints()


    def get_status_code(self):
        request = requests.get(Endpoints.getBookingById)
        status_code = request.status_code
        assert status_code == data.OK


    def get_valid_booking(self, id):
        request = requests.get(Endpoints.getBookingById + id)
        response = request.json()
        firstname = response.get("firstname")
        lastname = response.get("lastname")
        totalprice = response.get("totalprice")
        depositpaid = response.get("depositpaid")
        bookingdates = response.get("bookingdates")
        checkin = bookingdates.get("checkin")
        checkout = bookingdates.get("checkout")

        assert type(firstname) == str  # check if first name exists in response
        assert type(lastname) == str  # check if last name exists in response
        assert type(totalprice) == int  # check if total price exists in response
        assert type(depositpaid) == bool  # check if deposit paid exists in response
        assert type(checkin) == str  # check if checkin exists in response
        assert type(checkout) == str  # check if checkout exists in response


    def get_inValid_booking(self, id):
        request = requests.get(Endpoints.getBookingById + id)
        assert request.text == "Not Found"