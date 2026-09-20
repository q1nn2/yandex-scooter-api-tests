import allure
import requests

from urls import TRACK_ORDER


@allure.feature("Получение заказа по номеру")
class TestGetOrderByTrack:

    @allure.title("Заказ можно получить по его номеру")
    def test_get_order_by_track_success(self, order):
        response = requests.get(TRACK_ORDER, params={"t": order["track"]})

        assert response.status_code == 200
        assert "order" in response.json()
        assert response.json()["order"]["track"] == order["track"]

    @allure.title("Без номера заказа запрос возвращает ошибку")
    def test_get_order_without_track_error(self):
        response = requests.get(TRACK_ORDER)

        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для поиска"

    @allure.title("Несуществующий номер заказа возвращает ошибку")
    def test_get_order_with_nonexistent_track_error(self):
        response = requests.get(TRACK_ORDER, params={"t": 99999999})

        assert response.status_code == 404
        assert response.json()["message"] == "Заказ не найден"
