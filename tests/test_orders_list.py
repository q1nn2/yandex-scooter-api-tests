import allure

from api_methods import OrderMethods


@allure.feature("Список заказов")
class TestOrdersList:

    @allure.title("В ответе возвращается список заказов")
    def test_get_orders_list_success(self):
        response = OrderMethods.get_orders()

        assert response.status_code == 200
        assert "orders" in response.json()
        assert isinstance(response.json()["orders"], list)
