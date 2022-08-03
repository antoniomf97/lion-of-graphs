import http.client
import json
import base64


plotter_url = "localhost:8080"
fitter_url = "localhost:8081"


def get_data_from_file(filename):
    with open(filename, 'r') as file:
        data = base64.b64encode(bytes(file.read(), 'utf-8'))
    return data


def build_request(filename: str = "test.csv"):
    headers = {'Content-type': 'application/json'}
    body = {'Filename': 'test', 'ContentB64': get_data_from_file(filename).decode()}
    request = json.dumps(body)
    return request, headers


if __name__ == '__main__':
    connection = http.client.HTTPConnection(fitter_url)
    connection.request("POST", "/plotter", *build_request())
    response = connection.getresponse()

    print(response.read().decode())

    connection.close()
