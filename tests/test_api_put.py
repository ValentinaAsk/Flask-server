import datetime
import pytest
import requests
from app.data import dictionary
from tests.base_api import Base
from tests.scheme_and_data_for_tests import *


class TestPut(Base):

    def test_put_nonexistent_key_status_code(self, valid_data):
        """
        Проверка статуса ответа метода PUT при запросе к несуществющему ключу.
        Ожидаемый результат 404
        """
        request_data = valid_data
        key = request_data["key"]
        location = self.url + f'/{key}'

        response = requests.put(location, json=request_data)

        assert response.status_code == 404

    @pytest.mark.parametrize('request_data', InvalidDataClass.InvalidData)
    def test_put_invalid_data_status_code(self, request_data):
        """
        Проверка статуса ответа метода PUT при запросе с невалидными данными.
        Ожидаемый результат 400
        """
        key = 'invalid'
        try:
            key = request_data.get("key")
        except Exception:
            pass
        finally:
            location = self.url + f'/{key}'

            response = requests.put(location, json=request_data)

            assert response.status_code == 400

    def test_put_invalid_key(self, valid_data):
        """
        Проверка статуса ответа метода PUT при запросе к существющему ключу, но несуществующем ключом в теле запроса..
        Ожидаемый результат 404
        """
        request_data = valid_data
        location = self.url + f'/{request_data["key"]}'
        request_data['key'] = fake.word()

        response = requests.put(location, json=request_data)

        assert response.status_code == 404

    def test_put_time(self,  valid_exist_data_with_deletion_for_put):
        """
        Проверка данных ответа при запросе методом PUT.
        Ожидаемый результат - поле ответа 'time' возвращает время запроса
        """

        request_data = valid_exist_data_with_deletion_for_put
        key = request_data["key"]
        location = self.url + f'/{key}'

        response = requests.put(location, json=request_data)

        response_data = response.json()

        time_now = datetime.datetime.now(tz=None)
        time = time_now.strftime('%Y-%m-%d %H:%M')

        assert response_data['time'] == time

    def test_put_result(self, valid_exist_data_with_deletion_for_put):
        """
        Проверка данных ответа при запросе методом PUT.
        Ожидаемый результат - поле ответа 'result' возвращает значения из dictionary, которое было отправлено
        """
        request_data = valid_exist_data_with_deletion_for_put
        key = request_data['key']
        location = self.url + f'/{key}'

        response = requests.put(location, json=request_data)
        response_data = response.json()

        assert request_data['value'] == response_data['result']
        assert dictionary[key] == response_data['result']

    def test_put_exist_key_status_code(self, valid_exist_data_with_deletion_for_put):
        """
        Проверка статуса ответа метода PUT при запросе к существющему ключу.
        Ожидаемый результат 202
        """
        request_data = valid_exist_data_with_deletion_for_put
        key = request_data['key']
        location = self.url + f'/{key}'

        response = requests.put(location, json=request_data)

        assert response.status_code == 200

    def test_put(self, valid_exist_data_with_deletion_for_put):
        """
        Проверка обновления данных в dictionary при методе PUT.
        Ожидаемый результат - обновление в dictionary значения по ключу из запроса
        """
        request_data = valid_exist_data_with_deletion_for_put
        key = request_data['key']
        location = self.url + f'/{key}'

        requests.put(location, json=request_data)

        assert request_data['value'] == dictionary[key]

    def test_put_invalid_data_type(self, valid_exist_data_with_deletion_for_put):
        """
        Проверка статуса ответа метода PUT при отправлении данных в невалидном формате.
        Ожидаемый результат 400
        """
        request_data = valid_exist_data_with_deletion_for_put
        key = request_data['key']
        location = self.url + f'/{key}'

        response = requests.put(location, data=request_data)

        assert response.status_code == 400

    def test_two_put(self, valid_exist_data_with_deletion_for_put):
        """
        Два последовательных запроса методом PUT с одинаковыми данными.
        Проверка статуса ответа второго запроса.
        Ожидаемый результат 200
        """
        request_data = valid_exist_data_with_deletion_for_put
        key = request_data['key']
        location = self.url + f'/{key}'

        requests.put(location, json=request_data)

        request_2 = requests.put(location, json=request_data)

        assert request_2.status_code == 200
