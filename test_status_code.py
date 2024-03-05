# тесты проверяющие коды состояния ответов

import pytest
import requests

BASE_URL = "https://api.zippopotam.us/{country}/{postal_code}"


class TestStatusCodes:
    # корректный индекс
    @pytest.mark.parametrize("country, postal_code", [("US", "90210"), ("DE", "44137")])
    def test_status_code(self, country, postal_code):
        url = BASE_URL.format(country=country, postal_code=postal_code)
        response = requests.get(url)
        assert response.status_code == 200

    # некорректный клиентский запрос
    @pytest.mark.parametrize("country, postal_code", [("us", "0"), ("gb", "test")])
    def test_redirects(self, country, postal_code):
        url = BASE_URL.format(country=country, postal_code=postal_code, allow_redirects=False)
        response = requests.get(url)
        assert response.status_code == 404
