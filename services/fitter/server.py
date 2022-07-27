from http.server import SimpleHTTPRequestHandler
from http.server import HTTPServer
from ext_modules import config_logger
from ext_modules import logger
from service import service


hostName = "localhost"
serverPort = 8081


class FitterHandler(SimpleHTTPRequestHandler):
    def _set_headers(self, content_length):
        self.send_header('Content-type', 'text/html')
        self.send_header("Content-Length", content_length)
        self.end_headers()
        
    def do_GET(self):
        self.send_response(200)
        self._set_headers("0")

    def do_POST(self):
        logger.debug("Invoking POST operator for fitter engine.")
        content_length = int(self.headers.get("content-length", "0"))
        length = int(content_length) if content_length else 0

        logger.debug("Reading input request.")
        request = self.rfile.read(length)

        logger.debug("Processing fitter engine for given request.")
        response = service(request)

        logger.debug("Sending response: 200 - OK.")
        self.send_response(200)
        self._set_headers(str(len(response)))

        logger.debug("Retrieving response from engine.")
        self.wfile.write(response)
    
    do_PUT = do_POST
    do_DELETE = do_GET


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
