import allure
import pytest

from api_methods import CourierMethods
from helpers import generate_courier_data


@allure.feature("Создание курьера")
class TestCreateCourier:

    @allure.title("Курьера можно создать")
    def test_create_courier_success(self, courier_data):
        response = CourierMethods.create_courier(courier_data)

        assert response.status_code == 201
        assert response.json() == {"ok": True}

    @allure.title("Нельзя создать двух одинаковых курьеров")
    def test_create_duplicate_courier_error(self, courier):
        payload = {
            "login": courier["login"],
            "password": courier["password"],
            "firstName": courier["firstName"]
        }

        response = CourierMethods.create_courier(payload)

        assert response.status_code == 409
        assert response.json()["message"] == "Этот логин уже используется. Попробуйте другой."

    @allure.title("Без обязательного поля курьер не создаётся")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_create_courier_without_required_field_error(self, missing_field):
        payload = generate_courier_data()
        payload.pop(missing_field)

        response = CourierMethods.create_courier(payload)

        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи"
