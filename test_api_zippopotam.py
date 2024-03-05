# основной файл с тестами API
import requests


class TestsSmoke:
    base_url = "https://api.zippopotam.us/"

    # Корректный запрос с существующим индексом с 19ю элементами
    def test_existing_postal_code(self):
        response = requests.get(self.base_url + "in/110001")
        data = response.json()
        assert response.status_code == 200
        assert len(data['places']) == 19

    # несуществующий индекс
    def test_non_existing_postal_code(self):
        response = requests.get(self.base_url + "ru/000000")
        assert response.status_code == 404

    # без индекса
    def test_request_without_postal_code(self):
        response = requests.get(self.base_url + "fr/")
        assert response.status_code == 404

    # некорректный формат индекса
    def test_invalid_postal_code_format(self):
        response = requests.get(self.base_url + "de/abc")
        assert response.status_code == 404

    # некорректный формат страны
    def test_invalid_country_format(self):
        response = requests.get(self.base_url + "kg/110001")
        assert response.status_code == 404

    # некорректный формат URL
    def test_invalid_url_format(self):
        response = requests.get(self.base_url + "invalid_url")
        assert response.status_code == 404
