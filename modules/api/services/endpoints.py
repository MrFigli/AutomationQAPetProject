HOST = "https://restful-booker.herokuapp.com"

class Endpoints:

    getAllIds = HOST + "/booking"
    createToken = HOST + "/booking/auth"
    healthCheck = HOST + "/booking/ping"
    filterByName = HOST + "/booking?firstname="
    filterByLastName = HOST + "/booking?lastname="
    addLastName = HOST + "&lastname="
    filterByCheckinDate = HOST + "/booking?checkin="
    filterByCheckOutDate = HOST + "/booking?checkout="
    addCheckOutDate = HOST + "&checkout="
    getBookingById = HOST + "/booking/"