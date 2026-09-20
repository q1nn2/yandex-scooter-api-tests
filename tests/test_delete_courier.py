import allure
import requests

from urls import CREATE_COURIER


@allure.feature("Удаление курьера")
class TestDeleteCourier:

    @allure.title("Курьера можно удалить")
    def test_delete_courier_success(self, courier):
        response = requests.delete(f'{CREATE_COURIER}/{courier["id"]}')

        assert response.status_code == 200
        assert response.json() == {"ok": True}

    @allure.title("Без id курьера запрос возвращает ошибку")
    def test_delete_courier_without_id_error(self):
        response = requests.delete(f'{CREATE_COURIER}/')

        assert response.status_code == 400
        assert "message" in response.json()

    @allure.title("Несуществующего курьера удалить нельзя")
    def test_delete_nonexistent_courier_error(self):
        response = requests.delete(f'{CREATE_COURIER}/999999999999')

        assert response.status_code == 404
        assert "message" in response.json()
