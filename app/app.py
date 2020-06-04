import scheme
from flask import Flask, request, abort, make_response
from scheme import *
import datetime

data_scheme = Structure({
    'key': Text(nonempty=True),
    'value': Text(nonempty=True)
})

data = {
    "valentina": "bla",
    "sasha": 'llll'
}

app = Flask(__name__)


@app.route('/dictionary/<key>', methods=['GET'])
def get_dictionary(key: str):
    try:
        value = data["key"]
        time_request = datetime.datetime.now(tz=None)
        response = make_response({"result": value, "time": time_request.strftime("%Y-%m-%d %H:%M")})
        return response
    except KeyError:
        abort(404)


@app.route('/dictionary', methods=['POST'])
def post_dictionary():
    try:
        request_data = request.get_json()

        if data.get(request_data["key"]):
            abort(409)

        if data_scheme.validate(request_data):
            data.update(request_data)

        value = request_data["key"]
        data.update({request_data["key"]: request_data["value"]})
        time_request = datetime.datetime.now(tz=None)

        response = make_response({"result": value, "time": time_request.strftime("%Y-%m-%d %H:%M")})
        return response
    except scheme.exceptions.ValidationError:
        abort(400)


@app.route('/dictionary/<key>', methods=['PUT'])
def put_dictionary(key: str):
    try:
        request_data = request.get_json()

        if not data.get(request_data["key"]):
            abort(404)

        if data_scheme.validate(request_data):
            data.update(request_data)

        value = request_data["key"]
        data.update({request_data["key"]: request_data["value"]})
        time_request = datetime.datetime.now(tz=None)

        response = make_response({"result": value, "time": time_request.strftime("%Y-%m-%d %H:%M")})
        return response
    except scheme.exceptions.ValidationError:
        abort(400)


@app.route('/dictionary/<key>', methods=['DELETE'])
def get_dictionary(key: str):
    try:
        value = data.get(key)
        time_request = datetime.datetime.now(tz=None)
        response = make_response({"result": value, "time": time_request.strftime("%Y-%m-%d %H:%M")})
        return response
    except KeyError:
        abort(404)


if __name__ == '__main__':
    app.run(debug=True)
