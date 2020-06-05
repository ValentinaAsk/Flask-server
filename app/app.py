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
        value = data[key]
        time_request = datetime.datetime.now(tz=None)
        response = make_response({"result": value, "time": time_request.strftime("%Y-%m-%d %H:%M")})
        return response
    except KeyError:
        abort(404)


@app.route('/dictionary', methods=['POST'])
def post_dictionary():
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
    except SchemaError:
        abort(400)


@app.route('/dictionary/<key>', methods=['DELETE'])
def delete_dictionary(key: str):
    try:
        value = data.get(key)
        time_request = datetime.datetime.now(tz=None)
        response = make_response({"result": value, "time": time_request.strftime("%Y-%m-%d %H:%M")})
        return response
    except KeyError:
        abort(404)


if __name__ == '__main__':
    run()
