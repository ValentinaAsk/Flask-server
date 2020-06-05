import datetime
import pytest
from faker import Faker
import requests
from app.app import data
faker = Faker()

# @pytest.mark.skip
class TestGet:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, config):
        self.url = config

    def test_get_status_code(self):
        key = 'mail.ru'
        location = self.url + f'/{key}'

        response = requests.get(location)

        assert response.status_code == 200

    def test_get_result(self):
        key = 'mail.ru'
        location = self.url + f'/{key}'

        response = requests.get(location)
        response_data = response.json()

        assert response_data['result'] == data['mail.ru']

    def test_get_time(self):
        key = 'mail.ru'
        location = self.url + f'/{key}'

        response = requests.get(location)
        response_data = response.json()

        time_request = datetime.datetime.now(tz=None)
        time = time_request.strftime('%Y-%m-%d %H:%M')

        assert response_data['time'] == time

    def test_get_invalid(self):
        key = 'wrong'
        location = self.url + f'/{key}'

        response = requests.get(location)

        assert response.status_code == 404

