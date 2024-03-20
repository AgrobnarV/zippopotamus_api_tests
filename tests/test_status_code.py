# тесты проверяющие коды состояния ответов

import pytest
import requests
import allure


@pytest.fixture(scope="module")
def base_url():
    return "https://api.zippopotam.us/{country}/{postal_code}"


@allure.feature("API Testing")
@allure.story("Status Code Tests")
class TestStatusCodes:
    # корректный индекс
    @allure.title("Test Status Code for Valid Postal Codes")
    @pytest.mark.parametrize("country, postal_code", [("US", "90210"), ("DE", "44137")])
    def test_status_code(self, base_url, country, postal_code):
        url = base_url.format(country=country, postal_code=postal_code)
        response = requests.get(url)
        assert response.status_code == 200

    # некорректный клиентский запрос
    @allure.title("Test Status Code for Invalid Postal Codes")
    @pytest.mark.parametrize("country, postal_code", [("us", "0"), ("gb", "test")])
    def test_redirects(self, base_url, country, postal_code):
        url = base_url.format(country=country, postal_code=postal_code)
        response = requests.get(url)
        assert response.status_code == 404
