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
        return ids[:10]


    def get_booking_id_by_valid_name(self, name):
        request = requests.get(Endpoints.filterByName + name)
        response = request.json()
        ids = sorted(getIDsFromResponse(response))
        return ids


    def get_booking_id_by_valid_lastname(self, lastName):
        request = requests.get(Endpoints.filterByLastName + lastName)
        response = request.json()
        ids = sorted(getIDsFromResponse(response))
        return ids


    def get_booking_id_by_invalid_name(self, invalidName):
        request = requests.get(Endpoints.filterByName + invalidName)
        response = request.json()
        ids = sorted(getIDsFromResponse(response))
        return ids


    def get_booking_id_by_invalid_lastname(self, invalidLastName):
        request = requests.get(Endpoints.filterByLastName + invalidLastName)
        response = request.json()
        ids = sorted(getIDsFromResponse(response))
        return ids