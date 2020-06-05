import threading
from flask import Flask, request, abort, make_response
from schema import Schema, SchemaError
import datetime
import time
data_scheme = Schema({
    'key': str,
    'value': str
})


app = Flask(__name__)


def run():
    server = threading.Thread(target=app.run, kwargs={'host': '127.0.0.1', 'port': 5000})
    server.start()
    return server


def shutdown_app():
    terminate_func = request.environ.get('werkzeug.server.shutdown')
    if terminate_func:
        terminate_func()


@app.route('/shutdown')
def shutdown():
    shutdown_app()
    return ''


data = {
    'mail.ru': 'targer'
}


@app.route('/dictionary/<key>', methods=['GET'])
def get_dictionary(key: str):
    try:
        if not data.get(key, False):
            return make_response("404 error", 404)
        value = data[key]

        time_request = datetime.datetime.now(tz=None)
        response = make_response({"result": value, "time": time_request.strftime("%Y-%m-%d %H:%M")})

        return response
    except Exception as e:
        print(e)


@app.route('/dictionary', methods=['POST'])
def post_dictionary():
    try:
        request_data = request.get_json()

        if not data_scheme.is_valid(request_data):
            return make_response("400 error", 400)

        value = request_data["value"]
        key = request_data["key"]

        if data.get(key, False):
            return make_response("409 error", 409)

        data[key] = value

        time_request = datetime.datetime.now(tz=None)
        response = make_response({"result": value, "time": time_request.strftime("%Y-%m-%d %H:%M")})

        return response
    except Exception as e:
        print(e)


@app.route('/dictionary/<key>', methods=['PUT'])
def put_dictionary(key: str):
    try:
        request_data = request.get_json()

        if not data_scheme.is_valid(request_data):
            return make_response("400 error", 400)

        value = request_data["value"]
        request_key = request_data["key"]

        if key != request_key:
            return make_response("invalid data", 404)

        if not data.get(key, False):
            return make_response("404 error", 404)

        data[key] = value

        time_request = datetime.datetime.now(tz=None)

        response = make_response({"result": value, "time": time_request.strftime("%Y-%m-%d %H:%M")})
        return response
    except Exception as e:
        print(e)


@app.route('/dictionary/<key>', methods=['DELETE'])
def delete_dictionary(key: str):
    try:
        value = data.get(key, None)
        time_request = datetime.datetime.now(tz=None)
        response = make_response({"result": value, "time": time_request.strftime("%Y-%m-%d %H:%M")})
        return response
    except Exception as e:
        print(e)


if __name__ == '__main__':
    run()
