import pytest


@pytest.mark.change
def test_remove_name(user):
    user.name = ""
    assert user.name == ""

@pytest.mark.check
def test_name(user):
    assert user.name == "Viktor"


@pytest.mark.check
def test_lastName(user):
    assert user.lastName == "Relitskyi"

