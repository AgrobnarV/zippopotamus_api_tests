# основной файл с тестами API
import pytest
import requests
import allure


@pytest.fixture(scope="module")
def base_url():
    return "https://api.zippopotam.us/"


@allure.feature("API Testing")
@allure.story("Smoke Tests")
class TestsSmoke:
    def test_existing_postal_code(self, base_url):
        response = requests.get(base_url + "in/110001")
        data = response.json()
        assert response.status_code == 200
        assert len(data['places']) == 19

    def test_non_existing_postal_code(self, base_url):
        response = requests.get(base_url + "ru/000000")
        assert response.status_code == 404

    def test_request_without_postal_code(self, base_url):
        response = requests.get(base_url + "fr/")
        assert response.status_code == 404

    def test_invalid_postal_code_format(self, base_url):
        response = requests.get(base_url + "de/abc")
        assert response.status_code == 404

    def test_invalid_country_format(self, base_url):
        response = requests.get(base_url + "kg/110001")
        assert response.status_code == 404

    def test_invalid_url_format(self, base_url):
        response = requests.get(base_url + "invalid_url")
        assert response.status_code == 404
