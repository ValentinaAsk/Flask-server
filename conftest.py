import pytest
import requests

URL = "http://0.0.0.0:5000/dictionary"
from app import app


@pytest.fixture(scope='session')
def config():
    app.run()
    yield URL
    shutdown_url = f'http://127.0.0.1:5000/shutdown'
    requests.get(shutdown_url)
