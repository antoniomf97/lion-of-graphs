import os
from service import service
from http.server import HTTPServer
from intmodules import config_logger, logger, MPBRequestHandler
from binascii import Error as ReadingBase64Error
from intmodules import DuplicatedEntryError, NanValueFoundError
from jsonschema.exceptions import ValidationError


class FitterHandler(MPBRequestHandler):
    def do_POST(self):
        content_length = int(self.headers.get("content-length", "0"))
        length = int(content_length) if content_length else 0
        request = self.rfile.read(length)

        try:
            parsed_request = self._multipart_parser(request)
            response = service(parsed_request)
        except ReadingBase64Error:
            response = "Bad Request: ReadingBase64Error"
            self._return_400(response)
        except ValidationError:
            response = "Bad Request: SchemaValidationError"
            self._return_400(response)
        except NanValueFoundError:
            response = "Bad Request: NanValueFoundError"
            self._return_400(response)
        except DuplicatedEntryError:
            response = "Bad Request: DuplicatedEntryError"
            self._return_400(response)
        except ValueError:
            response = "Bad Request: ValueError"
            self._return_400(response)
        except Exception:
            response = "Oops: something went wrong"
            self._return_500(response)
        else:
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Content-Length', str(len(response)))
            self.end_headers()
            self.wfile.write(response)


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
