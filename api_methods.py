import allure
import requests

from urls import (
    CREATE_COURIER,
    LOGIN_COURIER,
    ORDERS,
    CANCEL_ORDER,
    ACCEPT_ORDER,
    TRACK_ORDER,
    FINISH_ORDER
)


class CourierMethods:

    @staticmethod
    @allure.step("Создать курьера")
    def create_courier(payload):
        return requests.post(CREATE_COURIER, data=payload)

    @staticmethod
    @allure.step("Авторизовать курьера")
    def login_courier(payload):
        return requests.post(LOGIN_COURIER, data=payload)

    @staticmethod
    @allure.step("Удалить курьера с id {courier_id}")
    def delete_courier(courier_id):
        return requests.delete(f'{CREATE_COURIER}/{courier_id}')

    @staticmethod
    @allure.step("Удалить курьера без id")
    def delete_courier_without_id():
        return requests.delete(CREATE_COURIER)


class OrderMethods:

    @staticmethod
    @allure.step("Создать заказ")
    def create_order(payload):
        return requests.post(ORDERS, json=payload)

    @staticmethod
    @allure.step("Получить список заказов")
    def get_orders():
        return requests.get(ORDERS)

    @staticmethod
    @allure.step("Отменить заказ с трек-номером {track}")
    def cancel_order(track):
        return requests.put(CANCEL_ORDER, params={"track": track})

    @staticmethod
    @allure.step("Получить заказ по трек-номеру {track}")
    def get_order_by_track(track):
        return requests.get(TRACK_ORDER, params={"t": track})

    @staticmethod
    @allure.step("Получить заказ без трек-номера")
    def get_order_without_track():
        return requests.get(TRACK_ORDER)

    @staticmethod
    @allure.step("Принять заказ {order_id} курьером {courier_id}")
    def accept_order(order_id, courier_id):
        return requests.put(
            f'{ACCEPT_ORDER}/{order_id}',
            params={"courierId": courier_id}
        )

    @staticmethod
    @allure.step("Принять заказ {order_id} без id курьера")
    def accept_order_without_courier_id(order_id):
        return requests.put(f'{ACCEPT_ORDER}/{order_id}')

    @staticmethod
    @allure.step("Принять заказ без id заказа курьером {courier_id}")
    def accept_order_without_order_id(courier_id):
        return requests.put(
            ACCEPT_ORDER,
            params={"courierId": courier_id}
        )

    @staticmethod
    @allure.step("Завершить заказ {order_id}")
    def finish_order(order_id):
        return requests.put(f'{FINISH_ORDER}/{order_id}')
