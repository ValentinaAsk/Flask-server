import datetime
from time import sleep
import pytest
from faker import Faker
import requests
from app.app import data
fake = Faker()


class InvalidData:
    data_1 = {'value': 'wrong'}
    data_2 = {'key': 'wrong'}
    data_3 = {'key': 'wrong', 'value': 'wrong', 'NEW': 'new'}
    data_4 = {}


class TestPost:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, config):
        self.url = config

    def test_put_unexist_key_status_code(self):
        key = fake.word()
        value = fake.word()
        request_data = {'key': key, 'value': value}

        location = self.url + f'/{key}'

        response = requests.put(location, json=request_data)

        assert response.status_code == 404

    @pytest.mark.parametrize('request_data', [InvalidData.data_1,
                                              InvalidData.data_2,
                                              InvalidData.data_3,
                                              InvalidData.data_4])
    def test_put_invalid_data_status_code(self, request_data):
        if not request_data.get("key", False):
            key = fake.word()
        else:
            key = request_data["key"]

        location = self.url + f'/{key}'

        response = requests.put(location, json=request_data)

        assert response.status_code == 400

    def test_put_invalid_key(self):
        key = fake.word()
        value = fake.word()
        request_data = {'key': key, 'value': value}

        key = fake.word()
        location = self.url + f'/{key}'

        response = requests.put(location, json=request_data)

        assert response.status_code == 404

    def test_put_time(self):
        key = 'mail.ru'
        value = fake.word()
        request_data = {'key': key, 'value': value}

        location = self.url + f'/{key}'

        response = requests.put(location, json=request_data)

        response_data = response.json()

        time_now = datetime.datetime.now(tz=None)
        time = time_now.strftime('%Y-%m-%d %H:%M')

        assert response_data['time'] == time

    def test_put_exist_key(self):
        key = 'mail.ru'
        value = fake.word()
        request_data = {'key': key, 'value': value}

        location = self.url + f'/{key}'
        response = requests.put(location, json=request_data)

        assert response.status_code == 200

    def test_put_invalid_data_type(self):
        key = 'mail.ru'
        value = fake.word()
        request_data = {'key': key, 'value': value}

        location = self.url + f'/{key}'

        response = requests.put(location, data=request_data)

        assert response.status_code == 400

    def test_put(self):
        key = 'mail.ru'
        value = fake.word()
        request_data = {'key': key, 'value': value}

        location = self.url + f'/{key}'
        response = requests.put(location, json=request_data)
        response_data = response.json()

        assert response_data['result'] == value == data[key]
