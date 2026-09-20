import allure
import requests

from helpers import finish_order
from urls import ACCEPT_ORDER


@allure.feature("Принятие заказа")
class TestAcceptOrder:

    @allure.title("Курьер может принять заказ")
    def test_accept_order_success(self, courier, order):
        response = requests.put(
            f'{ACCEPT_ORDER}/{order["id"]}',
            params={"courierId": courier["id"]}
        )

        try:
            assert response.status_code == 200
            assert response.json() == {"ok": True}
        finally:
            if response.status_code == 200:
                finish_order(order["id"])

    @allure.title("Без id курьера заказ принять нельзя")
    def test_accept_order_without_courier_id_error(self, order):
        response = requests.put(f'{ACCEPT_ORDER}/{order["id"]}')

        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для поиска"

    @allure.title("С неверным id курьера заказ принять нельзя")
    def test_accept_order_with_wrong_courier_id_error(self, order):
        response = requests.put(
            f'{ACCEPT_ORDER}/{order["id"]}',
            params={"courierId": 99999999}
        )

        assert response.status_code == 404
        assert response.json()["message"] == "Курьера с таким id не существует"

    @allure.title("Без id заказа запрос возвращает ошибку")
    def test_accept_order_without_order_id_error(self, courier):
        response = requests.put(
            ACCEPT_ORDER,
            params={"courierId": courier["id"]}
        )

        assert response.status_code == 404
        assert response.json()["message"] == "Not Found."

    @allure.title("С неверным id заказа запрос возвращает ошибку")
    def test_accept_order_with_wrong_order_id_error(self, courier):
        response = requests.put(
            f'{ACCEPT_ORDER}/99999999',
            params={"courierId": courier["id"]}
        )

        assert response.status_code == 404
        assert response.json()["message"] == "Заказа с таким id не существует"
