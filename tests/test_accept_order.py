import allure
import requests

from urls import ACCEPT_ORDER


@allure.feature("Принятие заказа")
class TestAcceptOrder:

    @allure.title("Курьер может принять заказ")
    def test_accept_order_success(self, courier_with_id, order):
        response = requests.put(
            f'{ACCEPT_ORDER}/{order["id"]}',
            params={"courierId": courier_with_id["id"]}
        )

        assert response.status_code == 200
        assert response.json() == {"ok": True}

    @allure.title("Без id курьера заказ принять нельзя")
    def test_accept_order_without_courier_id_error(self, order):
        response = requests.put(f'{ACCEPT_ORDER}/{order["id"]}')

        assert response.status_code == 400
        assert "message" in response.json()

    @allure.title("С неверным id курьера заказ принять нельзя")
    def test_accept_order_with_wrong_courier_id_error(self, order):
        response = requests.put(
            f'{ACCEPT_ORDER}/{order["id"]}',
            params={"courierId": 999999999999}
        )

        assert response.status_code == 404
        assert "message" in response.json()

    @allure.title("Без id заказа запрос возвращает ошибку")
    def test_accept_order_without_order_id_error(self, courier_with_id):
        response = requests.put(
            f'{ACCEPT_ORDER}/',
            params={"courierId": courier_with_id["id"]}
        )

        assert response.status_code == 400
        assert "message" in response.json()

    @allure.title("С неверным id заказа запрос возвращает ошибку")
    def test_accept_order_with_wrong_order_id_error(self, courier_with_id):
        response = requests.put(
            f'{ACCEPT_ORDER}/999999999999',
            params={"courierId": courier_with_id["id"]}
        )

        assert response.status_code == 404
        assert "message" in response.json()
