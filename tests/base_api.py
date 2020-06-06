import pytest
import requests

class Base:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, config):
        self.url = config
