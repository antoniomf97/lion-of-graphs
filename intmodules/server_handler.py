from http.server import SimpleHTTPRequestHandler

class MPBRequestHandler(SimpleHTTPRequestHandler):
    # define private methods for the most common returns with defaults
    # except the 200 -> that one should always be 100% handled by the actual
    # service handler class
    def _set_headers(self, content_length: int = 0):
        self.send_header('Content-type', 'text/plain')
        self.send_header("Content-Length", str(content_length))
        self.end_headers()

    def _return_201(self):
        self.send_response(201)
        self._set_headers()

    def _return_400(self, message: str = "Bad request"):
        self.send_response(400)
        self._set_headers(len(message))
        self.wfile.write(message.encode())

    def _return_405(self, message="Method is not allowed in this service"):
        self.send_response(405)
        self._set_headers(len(message))
        self.wfile.write(bytes(message))

    # Per default all methods are not implemented
    do_GET = _return_405
    do_HEAD = _return_405
    do_POST = _return_405
    do_PUT = _return_405
    do_DELETE = _return_405
    do_CONNECT = _return_405
    do_OPTIONS = _return_405
    do_TRACE = _return_405
    do_PATCH = _return_405


