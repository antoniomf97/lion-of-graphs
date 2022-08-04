import http.client
import json
import base64


plotter_url = "localhost:8080"
fitter_url = "localhost:8081"

path = "../tests/"


def get_data_csv(filename):
    with open(filename, 'r') as file:
        data = base64.b64encode(bytes(file.read(), 'utf-8'))
    return data


def get_data_json(filename):
    with open(filename, 'rb') as file:
        data = file.read()
    return data


def build_request_csv(filename: str = "test.csv"):
    headers = {'Content-type': 'application/json'}
    body = {'Filename': 'test', 'ContentB64': get_data_csv(path + filename).decode()}
    request = json.dumps(body)
    return request, headers


def build_request_json(filename: str = "test.json"):
    headers = {'Content-type': 'application/json'}
    body = get_data_json(path + filename)
    request = body
    return request, headers


if __name__ == '__main__':
    connection = http.client.HTTPConnection(plotter_url)
    connection.request("POST", "/plotter", *build_request_json("test_json_validation.json"))
    response = connection.getresponse()

    print(response.read().decode())

    connection.close()
