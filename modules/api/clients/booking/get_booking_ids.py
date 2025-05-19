import requests
from config import data
from modules.api.clients.booking.endpoints import Endpoints


def getIDsFromResponse(resp):
    id_array = []

    for key in resp:
        id_array.append(key.get("bookingid"))

    return id_array


class GetBookingIds:


    def __init__(self):
        self.endpoints = Endpoints()


    def get_status_code(self):
        request = requests.get(Endpoints.getAllIds)
        status_code = request.status_code
        assert status_code == data.OK


    def get_booking_ids(self):
        request = requests.get(Endpoints.getAllIds)
        response = request.json()
        ids = sorted(getIDsFromResponse(response))
        assert ids[:10] == data.all_ids


    def get_booking_id_by_valid_name(self, name):
        request = requests.get(Endpoints.filterByName + name)
        response = request.json()
        ids = sorted(getIDsFromResponse(response))
        assert len(ids) != 0
        assert type(ids[0]) == int


    def get_booking_id_by_valid_lastname(self, lastName):
        request = requests.get(Endpoints.filterByLastName + lastName)
        response = request.json()
        ids = sorted(getIDsFromResponse(response))
        assert len(ids) != 0
        assert type(ids[0]) == int


    def get_booking_id_by_invalid_name(self, invalidName):
        request = requests.get(Endpoints.filterByName + invalidName)
        response = request.json()
        ids = getIDsFromResponse(response)
        assert ids == []


    def get_booking_id_by_invalid_lastname(self, invalidLastName):
        request = requests.get(Endpoints.filterByLastName + invalidLastName)
        response = request.json()
        ids = getIDsFromResponse(response)
        assert ids == []


    def get_booking_id_by_valid_name_invalid_lastname(self, validName, invalidLastName):
        request = requests.get(Endpoints.filterByName + validName + Endpoints.addLastName + invalidLastName)
        response = request.json()
        ids = getIDsFromResponse(response)
        assert ids == []


    def get_booking_id_by_inValid_name_valid_lastname(self, inValidName, validLastName):
        request = requests.get(Endpoints.filterByName + inValidName + Endpoints.addLastName + validLastName)
        response = request.json()
        ids = getIDsFromResponse(response)
        assert ids == []


    def get_booking_by_checkinDate(self, checkinDate):
        request = requests.get(Endpoints.filterByCheckinDate + checkinDate)
        response = request.json()
        ids = getIDsFromResponse(response)
        assert len(ids) != 0
        assert type(ids[0]) == int


    def get_booking_by_checkOutDate(self, checkOutDate):
        request = requests.get(Endpoints.filterByCheckOutDate + checkOutDate)
        response = request.json()
        ids = getIDsFromResponse(response)
        assert len(ids) != 0
        assert type(ids[0]) == int


    def get_booking_by_invalid_checkinDate(self, invalidCheckinDate):
        request = requests.get(Endpoints.filterByCheckinDate + invalidCheckinDate)
        response = request.json()
        ids = getIDsFromResponse(response)
        assert ids == []


    def get_booking_by_invalid_dateFormat(self, invalidDateFormat):
        request = requests.get(Endpoints.filterByCheckinDate + invalidDateFormat)
        status_code = request.status_code
        assert status_code == data.INTERNAL_SERVER_ERROR