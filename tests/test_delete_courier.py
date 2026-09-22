import allure

from api_methods import CourierMethods


@allure.feature("Удаление курьера")
class TestDeleteCourier:

    @allure.title("Курьера можно удалить")
    def test_delete_courier_success(self, courier):
        response = CourierMethods.delete_courier(courier["id"])

        assert response.status_code == 200
        assert response.json() == {"ok": True}

    @allure.title("Без id курьера запрос возвращает ошибку")
    def test_delete_courier_without_id_error(self):
        response = CourierMethods.delete_courier_without_id()

        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для удаления курьера"

    @allure.title("Несуществующего курьера удалить нельзя")
    def test_delete_nonexistent_courier_error(self):
        response = CourierMethods.delete_courier(99999999)

        assert response.status_code == 404
        assert response.json()["message"] == "Курьера с таким id нет."
