import requests

from tests.base_api import Base
from app.data import dictionary
import datetime
from tests.scheme_and_data_for_tests import *


class TestGet(Base):

    def test_get_status_code(self, valid_exist_data_with_deletion):
        """
        Проверка статуса ответа метода GET при валидном запросе.
        Ожидаемый результат 200
        """
        key = valid_exist_data_with_deletion["key"]
        location = self.url + f'/{key}'

        response = requests.get(location)

        assert response.status_code == 200

    def test_get_nonexistent_key_status_code(self):
        """
        Проверка статуса ответа метода GET при запросе к несуществующему ключу.
        Ожидаемый результат 404
        """
        key = 'nonexistent'
        location = self.url + f'/{key}'

        response = requests.get(location)

        assert response.status_code == 404

    def test_get_scheme(self, valid_exist_data_with_deletion):
        """
        Проверка формата ответа сервера при запросе методом GET.
        Ожидаемый формат {'result': str, 'time': str}
        """
        key = valid_exist_data_with_deletion["key"]
        location = self.url + f'/{key}'

        response = requests.get(location, timeout=2)
        response_data = response.json()

        assert response_scheme.is_valid(response_data)

    def test_get_result(self, valid_exist_data_with_deletion):
        """
        Проверка данных ответа при запросе методом GET.
        Ожидаемый результат - поле ответа 'result' возвращает значения из dictionary
        """
        key = valid_exist_data_with_deletion["key"]
        location = self.url + f'/{key}'

        response = requests.get(location)
        response_data = response.json()

        assert response_data['result'] == dictionary[key]

    def test_get_time(self, valid_exist_data_with_deletion ):
        """
        Проверка данных ответа при запросе методом GET.
        Ожидаемый результат - поле ответа 'time' возвращает время запроса
        """
        key = valid_exist_data_with_deletion["key"]
        location = self.url + f'/{key}'

        response = requests.get(location)
        response_data = response.json()

        time_request = datetime.datetime.now(tz=None)
        time = time_request.strftime('%Y-%m-%d %H:%M')

        assert response_data['time'] == time



