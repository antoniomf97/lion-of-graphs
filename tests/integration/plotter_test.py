import unittest
import requests

plotter_url = "http://localhost:8080"


class TestStringMethods(unittest.TestCase):
    def test_successful_request(self):
        # gets the local data
        with open('../test.csv', 'rb') as file:
            data = file.read()

        # do the request to the plotter
        response = requests.post(
            plotter_url,
            files={
                'file': ('test.csv', data),
                'options': '''{
                    "color": "#0000FF",
                    "title": {"label": "Title", "color": "#666666", "fontsize": 12},
                    "xlabel": {"xlabel": "x", "loc": "center"},
                    "ylabel": {"ylabel": "y", "loc": "center"},
                    "grid": {"visible": true, "axis": "both"}
                }'''
            }
        )

        # expect a 200 and a defined plot
        self.assertEqual(response.status_code, 200)

        # TODO compare with reference image (but not by pixel)

    def test_invalid_method(self):
        response = requests.get(
            plotter_url
        )

        # expect a 405 on invalid method
        self.assertEqual(response.status_code, 405)


if __name__ == '__main__':
    unittest.main()
