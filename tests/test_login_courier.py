import allure
import requests

from helpers import generate_random_string
from urls import LOGIN_COURIER


@allure.feature("Логин курьера")
class TestLoginCourier:

    @allure.title("Курьер может авторизоваться")
    def test_login_courier_success(self, courier):
        response = requests.post(LOGIN_COURIER, data={
            "login": courier["login"],
            "password": courier["password"]
        })

        assert response.status_code == 200
        assert "id" in response.json()
        assert isinstance(response.json()["id"], int)

    @allure.title("Без обязательного поля авторизация не выполняется")
    def test_login_without_required_field_error(self, courier):
        response = requests.post(LOGIN_COURIER, data={
            "login": courier["login"]
        })

        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для входа"

    @allure.title("С неверным паролем авторизация не выполняется")
    def test_login_with_wrong_password_error(self, courier):
        response = requests.post(LOGIN_COURIER, data={
            "login": courier["login"],
            "password": generate_random_string(10)
        })

        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"

    @allure.title("Несуществующий курьер не может авторизоваться")
    def test_login_nonexistent_courier_error(self):
        response = requests.post(LOGIN_COURIER, data={
            "login": generate_random_string(20),
            "password": generate_random_string(20)
        })

        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"
