from schema import Schema, Or
from faker import Faker
fake = Faker()


class InvalidDataClass:
    data_1 = {'value': 'wrong'}
    data_2 = {'key': 'wrong'}
    data_3 = {'key': 'wrong', 'value': 'wrong', 'NEW': 'new'}
    data_4 = {}
    data_5 = ['key', 'value']
    InvalidData = [data_1, data_2, data_3, data_4, data_5]


RESPONSE_SCHEMA = Schema({
    'result': Or(str, None),
    'time': str
})
