from unittest import TestCase, main
from requests import post
from json import dumps


plotter_url = "http://localhost:8081/plotter"


# TODO: refactor services according to new data model


class TestStringMethods(TestCase):
    def test_basic_plot(self):
        with open("../test_basic.csv", "rb") as file:
            data = file.read()

        # do the request to the plotter
        response = post(
            plotter_url,
            files={
                "rawData": ("test_basic.csv", data, 'text/plain'),
                "rawPayload": (None, """{
                    "data": [{
                        "datatype": "file",
                        "filename": "test_basic.csv",
                        "column_names": {"y": "Y"}
                    }]
                }"""),
            }
        )

        # expect a 200 and a defined plot
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    main()
