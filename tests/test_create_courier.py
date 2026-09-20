import allure
import pytest
import requests

from helpers import generate_random_string, get_courier_id, delete_courier_by_id
from urls import CREATE_COURIER


@allure.feature("Создание курьера")
class TestCreateCourier:

    @allure.title("Курьера можно создать")
    def test_create_courier_success(self):
        payload = {
            "login": generate_random_string(10),
            "password": generate_random_string(10),
            "firstName": generate_random_string(10)
        }

        response = requests.post(CREATE_COURIER, data=payload)

        try:
            assert response.status_code == 201
            assert response.json() == {"ok": True}
        finally:
            if response.status_code == 201:
                courier_id = get_courier_id(payload["login"], payload["password"])
                delete_courier_by_id(courier_id)

    @allure.title("Нельзя создать двух одинаковых курьеров")
    def test_create_duplicate_courier_error(self, courier):
        payload = {
            "login": courier["login"],
            "password": courier["password"],
            "firstName": courier["firstName"]
        }

        response = requests.post(CREATE_COURIER, data=payload)

        assert response.status_code == 409
        assert response.json()["message"] == "Этот логин уже используется. Попробуйте другой."

    @allure.title("Без обязательного поля курьер не создаётся")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_create_courier_without_required_field_error(self, missing_field):
        payload = {
            "login": generate_random_string(10),
            "password": generate_random_string(10),
            "firstName": generate_random_string(10)
        }
        payload.pop(missing_field)

        response = requests.post(CREATE_COURIER, data=payload)

        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи"
