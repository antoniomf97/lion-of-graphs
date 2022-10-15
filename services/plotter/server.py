import os
from http.server import HTTPServer
from json import load
from jsonschema.exceptions import ValidationError
from service import service

from services.utils import MPBRequestHandler  # config_logger, logger,
from services.utils import InvalidRequestError


with open(os.path.join(".", "schema.json")) as f:
    PLOTTER_OPTIONS_SCHEMA = load(f)


class PlotterHandler(MPBRequestHandler):
    def do_POST(self):
        content_length = int(self.headers.get("content-length", "0"))
        length = int(content_length) if content_length else 0
        request = self.rfile.read(length)

        try:
            parsed_request = self._multipart_parser(request)
            response = service(parsed_request, PLOTTER_OPTIONS_SCHEMA)
        except (InvalidRequestError, ValidationError, ValueError) as e:
            response = "Bad Request: " + str(e)
            self._return_400(response)
        except Exception as e:
            response = "Oops: something went wrong...\n" + str(e)
            self._return_500(response)
        else:
            self.send_response(200)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Content-Type', 'image/png')
            self.send_header('Content-Length', str(response.getbuffer().nbytes))
            self.end_headers()
            self.wfile.write(response.getvalue())


if __name__ == "__main__":
    filename, level = "plotter.log", 10
    # config_logger(filename=filename, clean_logs=False)
    # logger.debug("Initialized logger for plotter service at {} with level {}.".format(filename, level))

    hostName = os.getenv('SERVER_HOSTNAME', 'localhost')
    serverPort = int(os.getenv('SERVER_PORT', 8080))

    webServer = HTTPServer((hostName, serverPort), PlotterHandler)
    print("Plotter server started at http://{}:{}".format(hostName, serverPort))
    # logger.debug("Plotter server started at http://{}:{}".format(hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        print("Server interrupted.")
        pass

    webServer.server_close()
    print("Plotter server stopped.")
    # logger.debug("Plotter server stopped.")
