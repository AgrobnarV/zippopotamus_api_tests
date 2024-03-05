# основной файл с тестами API
import requests
import allure


@allure.feature("API Testing")
@allure.story("Smoke Tests")
class TestsSmoke:
    base_url = "https://api.zippopotam.us/"

    @allure.title("Test Existing Postal Code")
    def test_existing_postal_code(self):
        response = requests.get(self.base_url + "in/110001")
        data = response.json()
        assert response.status_code == 200
        assert len(data['places']) == 19

    @allure.title("Test Non-existing Postal Code")
    def test_non_existing_postal_code(self):
        response = requests.get(self.base_url + "ru/000000")
        assert response.status_code == 404

    @allure.title("Test Request Without Postal Code")
    def test_request_without_postal_code(self):
        response = requests.get(self.base_url + "fr/")
        assert response.status_code == 404

    @allure.title("Test Invalid Postal Code Format")
    def test_invalid_postal_code_format(self):
        response = requests.get(self.base_url + "de/abc")
        assert response.status_code == 404

    @allure.title("Test Invalid Country Format")
    def test_invalid_country_format(self):
        response = requests.get(self.base_url + "kg/110001")
        assert response.status_code == 404

    @allure.title("Test Invalid URL Format")
    def test_invalid_url_format(self):
        response = requests.get(self.base_url + "invalid_url")
        assert response.status_code == 404
