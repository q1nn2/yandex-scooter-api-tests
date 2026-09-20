import allure
import pytest
import requests

from data import ORDER_COLORS, ORDER_DATA
from helpers import cancel_order
from urls import ORDERS


@allure.feature("Создание заказа")
class TestCreateOrder:

    @allure.title("Заказ создаётся с разными вариантами цвета")
    @pytest.mark.parametrize("color", ORDER_COLORS)
    def test_create_order_with_different_colors_success(self, color):
        payload = ORDER_DATA.copy()

        if color:
            payload["color"] = color

        response = requests.post(ORDERS, json=payload)

        try:
            assert response.status_code == 201
            assert "track" in response.json()
            assert isinstance(response.json()["track"], int)
        finally:
            if response.status_code == 201:
                cancel_order(response.json()["track"])
