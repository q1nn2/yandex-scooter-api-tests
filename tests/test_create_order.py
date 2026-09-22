import allure
import pytest

from api_methods import OrderMethods
from data import ORDER_COLORS, ORDER_DATA


@allure.feature("Создание заказа")
class TestCreateOrder:

    @allure.title("Заказ создаётся с разными вариантами цвета")
    @pytest.mark.parametrize("color_data", ORDER_COLORS)
    def test_create_order_with_different_colors_success(self, color_data):
        payload = {**ORDER_DATA, **color_data}

        response = OrderMethods.create_order(payload)

        assert response.status_code == 201
        assert "track" in response.json()
        assert isinstance(response.json()["track"], int)

        OrderMethods.cancel_order(response.json()["track"])
