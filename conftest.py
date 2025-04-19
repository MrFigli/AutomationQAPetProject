import pytest


class User:

    def __init__(self) -> None:
        self.name = None
        self.lastName = None


    def create(self):
        self.name = "Viktor"
        self.lastName = "Relitskyi"


    def remove(self):
        self.name = ""
        self.lastName = ""


@pytest.fixture
def user():
    user = User()
    user.create()

    yield user

    user.remove()