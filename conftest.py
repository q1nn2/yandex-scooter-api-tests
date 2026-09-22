import pytest

from api_methods import CourierMethods, OrderMethods
from data import ORDER_DATA
from helpers import generate_courier_data


@pytest.fixture
def courier():
    payload = generate_courier_data()
    CourierMethods.create_courier(payload)
    login_response = CourierMethods.login_courier({
        "login": payload["login"],
        "password": payload["password"]
    })
    courier_id = login_response.json()["id"]

    yield {
        "login": payload["login"],
        "password": payload["password"],
        "firstName": payload["firstName"],
        "id": courier_id
    }

    CourierMethods.delete_courier(courier_id)


@pytest.fixture
def courier_data():
    payload = generate_courier_data()

    yield payload

    login_response = CourierMethods.login_courier({
        "login": payload["login"],
        "password": payload["password"]
    })
    courier_id = login_response.json().get("id")
    CourierMethods.delete_courier(courier_id)


@pytest.fixture
def order():
    response = OrderMethods.create_order(ORDER_DATA.copy())
    track = response.json()["track"]
    order_response = OrderMethods.get_order_by_track(track)
    order_id = order_response.json()["order"]["id"]

    yield {
        "track": track,
        "id": order_id
    }

    OrderMethods.cancel_order(track)


@pytest.fixture
def order_to_accept():
    response = OrderMethods.create_order(ORDER_DATA.copy())
    track = response.json()["track"]
    order_response = OrderMethods.get_order_by_track(track)
    order_id = order_response.json()["order"]["id"]

    yield {
        "track": track,
        "id": order_id
    }

    OrderMethods.finish_order(order_id)
    OrderMethods.cancel_order(track)
