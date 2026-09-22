import allure
import pytest

from api_methods import CourierMethods
from helpers import generate_random_string


@allure.feature("Логин курьера")
class TestLoginCourier:

    @allure.title("Курьер может авторизоваться")
    def test_login_courier_success(self, courier):
        response = CourierMethods.login_courier({
            "login": courier["login"],
            "password": courier["password"]
        })

        assert response.status_code == 200
        assert "id" in response.json()
        assert isinstance(response.json()["id"], int)

    @allure.title("Без обязательного поля авторизация не выполняется")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_login_without_required_field_error(self, courier, missing_field):
        payload = {
            "login": courier["login"],
            "password": courier["password"]
        }
        payload.pop(missing_field)

        response = CourierMethods.login_courier(payload)

        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для входа"

    @allure.title("С неверным логином или паролем авторизация не выполняется")
    @pytest.mark.parametrize("wrong_field", ["login", "password"])
    def test_login_with_wrong_credentials_error(self, courier, wrong_field):
        payload = {
            "login": courier["login"],
            "password": courier["password"]
        }
        payload[wrong_field] = generate_random_string(20)

        response = CourierMethods.login_courier(payload)

        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"

    @allure.title("Несуществующий курьер не может авторизоваться")
    def test_login_nonexistent_courier_error(self):
        response = CourierMethods.login_courier({
            "login": generate_random_string(20),
            "password": generate_random_string(20)
        })

        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"
