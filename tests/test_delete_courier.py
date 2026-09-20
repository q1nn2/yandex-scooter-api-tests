import allure
import requests

from helpers import generate_random_string
from urls import CREATE_COURIER


@allure.feature("Удаление курьера")
class TestDeleteCourier:

    @allure.title("Курьера можно удалить")
    def test_delete_courier_success(self, courier_with_id):
        response = requests.delete(f'{CREATE_COURIER}/{courier_with_id["id"]}')

        assert response.status_code == 200
        assert response.json() == {"ok": True}

    @allure.title("Без id курьера запрос возвращает ошибку")
    def test_delete_courier_without_id_error(self):
        response = requests.delete(f'{CREATE_COURIER}/')

        assert response.status_code == 400
        assert "message" in response.json()

    @allure.title("Несуществующего курьера удалить нельзя")
    def test_delete_nonexistent_courier_error(self):
        nonexistent_id = 999999999999
        response = requests.delete(f'{CREATE_COURIER}/{nonexistent_id}')

        assert response.status_code == 404
        assert "message" in response.json()
