import os
from http.server import HTTPServer

from jsonschema.exceptions import ValidationError
from service import service

from utils.server_handler import MPBRequestHandler  # config_logger, logger,
from utils.exceptions import InvalidRequestError


class FitterHandler(MPBRequestHandler):
    def do_POST(self):
        content_length = int(self.headers.get("content-length", "0"))
        length = int(content_length) if content_length else 0
        request = self.rfile.read(length)

        try:
            parsed_request = self._multipart_parser(request)
            response = service(parsed_request)
        except (InvalidRequestError, ValidationError, ValueError) as e:
            response = "Bad Request: " + str(e)
            self._return_400(response)
        except Exception:
            response = "Oops: something went wrong"
            self._return_500(response)
        else:
            self.send_response(200)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Content-type', 'image/png')
            self.send_header('Content-Length', str(response.getbuffer().nbytes))
            self.end_headers()
            self.wfile.write(response.getvalue())


if __name__ == "__main__":
    filename, level = "fitter.log", 10
    # config_logger(filename=filename)
    # logger.debug("Initialized logger for plotter service at {} with level {}.".format(filename, level))

    hostName = os.getenv('SERVER_HOSTNAME', 'localhost')
    serverPort = int(os.getenv('SERVER_PORT', 8081))

    webServer = HTTPServer((hostName, serverPort), FitterHandler)
    print("Fitter server started at http://{}:{}".format(hostName, serverPort))
    # logger.debug("Fitter server started at http://{}:{}".format(hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Fitter server stopped.")
    # logger.debug("Fitter server stopped.")
