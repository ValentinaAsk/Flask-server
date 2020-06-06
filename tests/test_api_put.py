import datetime
import pytest
import requests
from app.data import dictionary
from tests.base_api import Base
from tests.scheme_and_data_for_tests import *


@pytest.mark.skip
class TestPut(Base):

    def test_put_nonexistent_key_status_code(self, valid_data):
        request_data = valid_data
        key = request_data["key"]
        location = self.url + f'/{key}'

        response = requests.put(location, json=request_data)

        assert response.status_code == 404

    @pytest.mark.parametrize('request_data', InvalidDataClass.InvalidData)
    def test_put_invalid_data_status_code(self, request_data):
        key = 'invalid'
        try:
            key = request_data["key"]
        finally:
            location = self.url + f'/{key}'

            response = requests.put(location, json=request_data)

            assert response.status_code == 400

    def test_put_invalid_key(self, valid_data):
        request_data = valid_data

        key = fake.word()
        location = self.url + f'/{key}'

        response = requests.put(location, json=request_data)

        assert response.status_code == 404

    def test_put_time(self,  valid_exist_data_with_deletion_for_put):
        request_data = valid_exist_data_with_deletion_for_put
        key = request_data["key"]

        location = self.url + f'/{key}'

        response = requests.put(location, json=request_data)

        response_data = response.json()

        time_now = datetime.datetime.now(tz=None)
        time = time_now.strftime('%Y-%m-%d %H:%M')

        assert response_data['time'] == time

    def test_put_result(self, valid_exist_data_with_deletion_for_put):
        request_data = valid_exist_data_with_deletion_for_put
        key = request_data['key']

        location = self.url + f'/{key}'
        response = requests.put(location, json=request_data)
        response_data = response.json()

        assert request_data['value'] == response_data['result']
        assert dictionary[key] == response_data['result']

    def test_put_exist_key_status_code(self, valid_exist_data_with_deletion_for_put):
        request_data = valid_exist_data_with_deletion_for_put
        key = request_data['key']

        location = self.url + f'/{key}'
        response = requests.put(location, json=request_data)

        assert response.status_code == 200

    def test_put(self, valid_exist_data_with_deletion_for_put):
        request_data = valid_exist_data_with_deletion_for_put
        key = request_data['key']

        location = self.url + f'/{key}'
        requests.put(location, json=request_data)

        assert request_data['value'] == dictionary[key]

    def test_put_invalid_data_type(self, valid_exist_data_with_deletion_for_put):
        request_data = valid_exist_data_with_deletion_for_put
        key = request_data['key']

        location = self.url + f'/{key}'
        response = requests.put(location, data=request_data)

        assert response.status_code == 400

    def test_two_put(self, valid_exist_data_with_deletion_for_put):
        request_data = valid_exist_data_with_deletion_for_put
        key = request_data['key']

        location = self.url + f'/{key}'
        requests.put(location, json=request_data)

        request_2 = requests.put(location, json=request_data)

        assert request_2.status_code == 200
