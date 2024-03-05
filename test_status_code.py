# тесты проверяющие коды состояния ответов

import pytest
import requests
import allure

BASE_URL = "https://api.zippopotam.us/{country}/{postal_code}"


@allure.feature("API Testing")
@allure.story("Status Code Tests")
class TestStatusCodes:
    # корректный индекс
    @allure.title("Test Status Code for Valid Postal Codes")
    @pytest.mark.parametrize("country, postal_code", [("US", "90210"), ("DE", "44137")])
    def test_status_code(self, country, postal_code):
        url = BASE_URL.format(country=country, postal_code=postal_code)
        response = requests.get(url)
        assert response.status_code == 200

    # некорректный клиентский запрос
    @allure.title("Test Status Code for Invalid Postal Codes")
    @pytest.mark.parametrize("country, postal_code", [("us", "0"), ("gb", "test")])
    def test_redirects(self, country, postal_code):
        url = BASE_URL.format(country=country, postal_code=postal_code)
        response = requests.get(url)
        assert response.status_code == 404

    if __name__ == "__main__":
        pytest.main(['-v', '--html=report.html'])
