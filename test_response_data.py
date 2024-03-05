# тесты проверяющие содержимое ответов (например, наличие ключевых полей и их значения)

import pytest
import requests
import allure

BASE_URL = "https://api.zippopotam.us/{country}/{postal_code}"


@allure.feature("API Testing")
@allure.story("Response Content Tests")
class TestRequestData:
    @allure.title("Test Request Headers")
    @pytest.mark.parametrize("country, postal_code", [("us", "99950")])
    def test_request_headers(self, country, postal_code):
        url = BASE_URL.format(country=country, postal_code=postal_code)
        response = requests.get(url)
        assert response.url == url, "URL заголовка Host отличается от URL запроса"
        assert response.request.headers["User-Agent"], "заголовок User-Agent отсутствует"
        assert response.request.headers["Accept-Encoding"] == "gzip, deflate", "запрос не поддерживает сжатие контента"
        assert "Date" in response.headers


@allure.feature("API Testing")
@allure.story("Response Data Tests")
class TestResponseData:
    @allure.title("Test Response Headers")
    @pytest.mark.parametrize("country, postal_code", [("ar", "1657")])
    def test_response_headers(self, country, postal_code):
        url = BASE_URL.format(country=country, postal_code=postal_code)
        response = requests.get(url)

        assert response.headers["Content-Type"] == "application/json", "неверный формат ответа"
        assert response.headers["Content-Encoding"] == "gzip", "запрос не поддерживает сжатие контента"
        assert response.headers['Charset'] == 'UTF-8', "неверная кодировка ответа"

    @allure.title("Test Response Data")
    @pytest.mark.parametrize("country, postal_code", [("fr", "75001")])
    def test_response_data(self, country, postal_code):
        url = BASE_URL.format(country=country, postal_code=postal_code)
        response = requests.get(url)
        data = response.json()
        assert data['post code'] == '75001', "Некорректный индекс страны"
        assert data['country abbreviation'] == 'FR', "Некорректная аббревиатура страны"
        assert data['country'] == 'France', "Некорректное название страны"
        assert 'places' in data, "Внутри ответа отсутствуют данные по местоположению"
        assert data['places'][0]['place name'] == 'Paris 01 Louvre', "В ответе отсутствует название нас. пункта"
        assert data['places'][0]['longitude'] == '2.3417'
        assert data['places'][0]['state'] == '\u00cele-de-France'
        assert data['places'][0]['state abbreviation'] == 'A8'
        assert data['places'][0]['latitude'] == '48.8592'

    @allure.title("Test Response Size")
    @pytest.mark.parametrize("country, postal_code", [("br", "01000-000")])
    def test_response_size(self, country, postal_code):
        url = BASE_URL.format(country=country, postal_code=postal_code)
        response = requests.get(url)
        assert len(response.content) > 0, "ответ пустой и не содержит данных"

    if __name__ == "__main__":
        pytest.main(['-v', '--html=report.html'])
