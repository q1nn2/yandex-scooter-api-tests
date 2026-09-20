import pytest

from helpers import (
    create_courier,
    delete_courier_by_id,
    get_courier_id,
    create_order,
    get_order_id,
    cancel_order
)


@pytest.fixture
def courier():
    login, password, first_name = create_courier()
    courier_id = get_courier_id(login, password)

    yield {
        "login": login,
        "password": password,
        "firstName": first_name,
        "id": courier_id
    }

    delete_courier_by_id(courier_id)


@pytest.fixture
def order():
    track = create_order()

    yield {
        "track": track,
        "id": get_order_id(track)
    }

    cancel_order(track)
