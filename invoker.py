from audioop import mul
import http.client
import json
import base64


plotter_url = "localhost:8080"
fitter_url = "localhost:8081"
path = "./tests/"


def get_data_csv(filename):
    with open(filename, 'r') as file:
        data = base64.b64encode(bytes(file.read(), 'utf-8'))
    return data


def get_data_json(filename):
    with open(filename, 'r') as file:
        data = file.read()
    return data


def build_request_csv(filename: str = "test.csv"):
    headers = {'Content-type': 'application/json'}
    body = {'Filename': 'test', 'ContentB64': get_data_csv(path + filename).decode()}
    request = json.dumps(body)
    return request, headers


def build_request_json(filename: str = "test"):
    headers = {'Content-type': 'application/json'}
    body = get_data_json(path + filename + ".json")
    return body
    request = body
    return request, headers


if __name__ == '__main__':
    connection = http.client.HTTPConnection(plotter_url)
    
    # body, header = urllib3.encode_multipart_formdata(files)
    # multipart_data = MultipartDecoder.from_response(body)
    # print(multipart_data)

    with open(path + "test.csv", "rb") as f:
        file = f


    headers = {'Content-type': "multipart/form-data;"}
    connection.request("POST", "/plotter", body=files, headers=headers)
    response = connection.getresponse()

    print(response.read().decode())

    connection.close()
