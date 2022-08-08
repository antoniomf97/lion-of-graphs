from http.server import HTTPServer
from intmodules import config_logger, logger, MPBRequestHandler
from service import service


hostName = "localhost"
serverPort = 8081


class FitterHandler(MPBRequestHandler):
    def do_POST(self):
        content_length = int(self.headers.get("content-length", "0"))
        length = int(content_length) if content_length else 0
        request = self.rfile.read(length)

        try:
            response = service(request)
        except Exception:
            response = "Bad request"
            self._return_400(response)
        else:
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Content-Length', str(len(response)))
            self.end_headers()
            self.wfile.write(response)


if __name__ == "__main__":
    filename, level = "fitter.log", 10
    config_logger(filename=filename)
    logger.debug("Initialized logger for plotter service at {} with level {}.".format(filename, level))

    webServer = HTTPServer((hostName, serverPort), FitterHandler)
    print("Fitter server started at http://{}:{}".format(hostName, serverPort))
    logger.debug("Fitter server started at http://{}:{}".format(hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Fitter server stopped.")
    logger.debug("Fitter server stopped.")
