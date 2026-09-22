import allure

from api_methods import OrderMethods


@allure.feature("Принятие заказа")
class TestAcceptOrder:

    @allure.title("Курьер может принять заказ")
    def test_accept_order_success(self, courier, accepted_order):
        response = OrderMethods.accept_order(
            accepted_order["id"],
            courier["id"]
        )

        assert response.status_code == 200
        assert response.json() == {"ok": True}

    @allure.title("Без id курьера заказ принять нельзя")
    def test_accept_order_without_courier_id_error(self, order):
        response = OrderMethods.accept_order_without_courier_id(order["id"])

        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для поиска"

    @allure.title("С неверным id курьера заказ принять нельзя")
    def test_accept_order_with_wrong_courier_id_error(self, order):
        response = OrderMethods.accept_order(order["id"], 99999999)

        assert response.status_code == 404
        assert response.json()["message"] == "Курьера с таким id не существует"

    @allure.title("Без id заказа запрос возвращает ошибку")
    def test_accept_order_without_order_id_error(self, courier):
        response = OrderMethods.accept_order_without_order_id(courier["id"])

        assert response.status_code == 404
        assert response.json()["message"] == "Not Found."

    @allure.title("С неверным id заказа запрос возвращает ошибку")
    def test_accept_order_with_wrong_order_id_error(self, courier):
        response = OrderMethods.accept_order(99999999, courier["id"])

        assert response.status_code == 404
        assert response.json()["message"] == "Заказа с таким id не существует"
