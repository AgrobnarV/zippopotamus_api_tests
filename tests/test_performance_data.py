# тесты, проверяющие производительность запросов

import pytest
import requests
import time
import allure


@pytest.fixture(scope="module")
def base_url():
    return "https://api.zippopotam.us/{country}/{postal_code}"


@allure.feature("API Testing")
@allure.story("Performance Tests")
class TestPerformanceRequests:

    # время выполнение запроса
    @allure.title("Test API Performance")
    @pytest.mark.parametrize("country, postal_code", [("US", "10001"), ("sk", "900 84"), ("in", "854318")])
    def test_api_performance(self, base_url, country, postal_code):
        url = base_url.format(country=country, postal_code=postal_code)

        # сравниваем время запроса с пороговым значением в мс
        start_time = time.time()
        response = requests.get(url)
        end_time = time.time()
        execution_time = end_time - start_time
        max_allowed_time = 1.3

        assert response.status_code == 200
        assert execution_time < max_allowed_time, f"Запрос выполнился больше чем за : {execution_time} секунд"
