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


class TestPost:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, config):
        self.url = config

    def test_post_status_code(self):
        key = fake.word()
        value = fake.word()
        request_data = {'key': key, 'value': value}

        location = self.url

        response = requests.post(location, json=request_data)
        print(response, response.content, response.request.headers)

        assert response.status_code == 200

    @pytest.mark.parametrize('request_data', [InvalidData.data_1,
                                              InvalidData.data_2,
                                              InvalidData.data_3])
    def test_post_invalid_data_status_code(self, request_data):
        location = self.url

        response = requests.post(location, json=request_data)

        assert response.status_code == 400

    def test_post(self):
        key = fake.word()
        value = fake.word()
        request_data = {'key': key, 'value': value}

        location = self.url

        response = requests.post(location, json=request_data)
        response_data = response.json()

        assert data[key] == value == response_data["result"]

    def test_post_time(self):
        key = fake.word()
        value = fake.word()
        request_data = {'key': key, 'value': value}

        location = self.url

        response = requests.post(location, json=request_data)

        response_data = response.json()

        time_now = datetime.datetime.now(tz=None)
        time = time_now.strftime('%Y-%m-%d %H:%M')

        assert response_data['time'] == time

    def test_post_exist_key(self):
        key = 'mail.ru'
        value = 'new'
        request_data = {'key': key, 'value': value}

        location = self.url
        response = requests.post(location, json=request_data)

        assert response.status_code == 409

