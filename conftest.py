import pytest
import requests

from helpers import create_courier, delete_courier, get_courier_id, create_order, get_order_id
from urls import ORDERS


@pytest.fixture
def courier():
    login, password, first_name = create_courier()

    yield {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    delete_courier(login, password)


@pytest.fixture
def courier_with_id():
    login, password, first_name = create_courier()
    courier_id = get_courier_id(login, password)

    yield {
        "login": login,
        "password": password,
        "firstName": first_name,
        "id": courier_id
    }

    delete_courier(login, password)


@pytest.fixture
def order():
    track = create_order()
    order_data = {
        "track": track,
        "id": get_order_id(track)
    }

    yield order_data

    try:
        requests.put(f'{ORDERS}/cancel', params={"track": track}, timeout=5)
    except requests.RequestException:
        pass
