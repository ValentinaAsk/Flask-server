import pytest
import requests
from faker import Faker
fake = Faker()
from app import app
from app.data import dictionary


@pytest.fixture(scope='session')
def config():
    server = app.run()
    server_host = server._kwargs['host']
    server_port = server._kwargs['port']

    yield f'http://{server_host}:{server_port}/dictionary'

    shutdown_url = f'http://{server_host}:{server_port}/shutdown'
    requests.get(shutdown_url)


@pytest.fixture(scope='function')
def valid_exist_data_with_deletion():
    key = fake.word()
    value = fake.word()
    request_data = {'key': key, 'value': value}

    dictionary.update({key: value})

    yield request_data

    dictionary.pop(key)


@pytest.fixture(scope='function')
def valid_exist_data_without_deletion():
    key = fake.word()
    value = fake.word()
    request_data = {'key': key, 'value': value}

    dictionary.update({key: value})

    return request_data


@pytest.fixture(scope='function')
def valid_data():
    key = fake.word()
    value = fake.word()
    request_data = {'key': key, 'value': value}

    return request_data


@pytest.fixture(scope='function')
def valid_data_with_deletion():
    key = fake.word()
    value = fake.word()
    request_data = {'key': key, 'value': value}

    yield request_data

    dictionary.pop(key)


@pytest.fixture(scope='function')
def valid_exist_data_with_deletion_for_put():
    key = fake.word()
    value = fake.word()

    dictionary.update({key: value})

    request_data = {'key': key, 'value': fake.word()}

    yield request_data

    dictionary.pop(key)
