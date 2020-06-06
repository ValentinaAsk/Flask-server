import datetime
import pytest
import requests
from app.data import dictionary
from tests.base_api import Base
from tests.scheme_and_data_for_tests import *


@pytest.mark.skip
class TestPost(Base):

    def test_post_status_code(self, valid_data_with_deletion):
        request_data = valid_data_with_deletion
        location = self.url

        response = requests.post(location, json=request_data)

        assert response.status_code == 200

    @pytest.mark.parametrize('request_data', InvalidDataClass.InvalidData)
    def test_post_invalid_data_status_code(self, request_data):
        location = self.url

        response = requests.post(location, json=request_data)

        assert response.status_code == 400

    def test_post(self, valid_data_with_deletion):
        request_data = valid_data_with_deletion
        location = self.url

        requests.post(location, json=request_data)

        assert dictionary[request_data['key']] == request_data['value']

    def test_post_result(self, valid_data_with_deletion):
        request_data = valid_data_with_deletion
        location = self.url

        response = requests.post(location, json=request_data)
        response_data = response.json()

        assert response_data['result'] == request_data['value']
        assert dictionary[request_data['key']] == response_data['result']

    def test_post_time(self, valid_data_with_deletion):
        request_data = valid_data_with_deletion
        location = self.url

        response = requests.post(location, json=request_data)
        response_data = response.json()

        time_now = datetime.datetime.now(tz=None)
        time = time_now.strftime('%Y-%m-%d %H:%M')

        assert response_data['time'] == time

    def test_post_exist_key(self, valid_exist_data_without_deletion):
        request_data = valid_exist_data_without_deletion
        location = self.url

        response = requests.post(location, json=request_data)

        assert response.status_code == 409

    def test_post_invalid_data_type(self, valid_data):
        request_data = valid_data
        location = self.url

        response = requests.post(location, data=request_data)

        assert response.status_code == 400

    def test_post_scheme(self, valid_data_with_deletion):
        request_data = valid_data_with_deletion
        location = self.url

        response = requests.post(location, json=request_data)
        response_data = response.json()

        assert response_scheme.is_valid(response_data)

    def test_two_post(self, valid_data_with_deletion):
        request_data = valid_data_with_deletion
        location = self.url

        requests.post(location, json=request_data)

        response_2 = requests.post(location, json=request_data)

        assert response_2.status_code == 409
