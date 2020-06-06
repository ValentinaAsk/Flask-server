import datetime
import pytest
import requests
from tests.base_api import Base
from app.data import dictionary
from tests.scheme_and_data_for_tests import *


@pytest.mark.skip
class TestDelete(Base):

    def test_delete_status_code(self, valid_exist_data_without_deletion):
        key = valid_exist_data_without_deletion["key"]
        location = self.url + f'/{key}'

        response = requests.delete(location)

        assert response.status_code == 200

    def test_delete_data(self, valid_exist_data_without_deletion):
        key = valid_exist_data_without_deletion["key"]
        location = self.url + f'/{key}'

        requests.delete(location)

        assert dictionary.get(key) is None

    def test_delete_nonexistant_key_data(self):
        key = fake.word()
        location = self.url + f'/{key}'

        response = requests.delete(location)

        assert response.status_code == 200

    def test_delete_result(self, valid_exist_data_without_deletion):
        key = valid_exist_data_without_deletion["key"]
        location = self.url + f'/{key}'

        response = requests.delete(location)
        response_data = response.json()

        assert response_data['result'] is None

    def test_delete_time(self, valid_exist_data_without_deletion):
        key = valid_exist_data_without_deletion["key"]
        location = self.url + f'/{key}'

        response = requests.delete(location)
        response_data = response.json()

        time_request = datetime.datetime.now(tz=None)
        time = time_request.strftime('%Y-%m-%d %H:%M')

        assert response_data['time'] == time

    def test_delete_scheme(self, valid_exist_data_without_deletion):
        key = valid_exist_data_without_deletion["key"]
        location = self.url + f'/{key}'

        response = requests.delete(location)
        response_data = response.json()

        assert response_scheme.is_valid(response_data)
