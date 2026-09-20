import pytest

from helpers import create_courier, delete_courier


@pytest.fixture
def courier():
    login, password, first_name = create_courier()

    yield {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    delete_courier(login, password)
