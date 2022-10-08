import os
from service import service
from http.server import HTTPServer
from intmodules import MPBRequestHandler  # config_logger, logger,
from intmodules import InvalidRequestError
from jsonschema.exceptions import ValidationError


class PlotterHandler(MPBRequestHandler):
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
            self.send_header('Content-Type', 'image/png')
            self.send_header('Content-Length', str(len(response)))
            self.end_headers()
            self.wfile.write(response)

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST")
        self.send_header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Content-Length")
        self.end_headers()
        # self.wfile.write()


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
