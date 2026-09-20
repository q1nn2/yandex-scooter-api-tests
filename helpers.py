import random
import string
import requests

from data import ORDER_DATA
from urls import CREATE_COURIER, LOGIN_COURIER, ORDERS


def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


def register_new_courier_and_return_login_password():
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post(CREATE_COURIER, data=payload)

    if response.status_code == 201:
        return [login, password, first_name]

    return []


def create_courier():
    courier = register_new_courier_and_return_login_password()
    if not courier:
        raise RuntimeError("Не удалось создать тестового курьера")
    return courier


def get_courier_id(login, password):
    response = requests.post(LOGIN_COURIER, data={
        "login": login,
        "password": password
    })
    return response.json()["id"]


def delete_courier_by_id(courier_id):
    return requests.delete(f'{CREATE_COURIER}/{courier_id}')


def delete_courier(login, password):
    return delete_courier_by_id(get_courier_id(login, password))


def create_order():
    response = requests.post(ORDERS, json=ORDER_DATA.copy())
    if response.status_code != 201:
        raise RuntimeError("Не удалось создать тестовый заказ")
    return response.json()["track"]


def get_order_by_track(track):
    return requests.get(f'{ORDERS}/track', params={"t": track})


def get_order_id(track):
    return get_order_by_track(track).json()["order"]["id"]
