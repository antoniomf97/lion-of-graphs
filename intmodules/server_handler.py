from http.server import SimpleHTTPRequestHandler


class MPBRequestHandler(SimpleHTTPRequestHandler):
    def _set_headers(self, content_length: int = 0):
        """Sets the response headers for the give content_length"""
        self.send_header('Content-type', 'text/plain')
        self.send_header("Content-Length", str(content_length))
        self.end_headers()

    def _return_400(self, message: str = "	Bad Request"):
        """Sends a response with status code 400 - Bad Request"""
        self.send_response(400)
        self._set_headers(len(message))
        self.wfile.write(message.encode())

    def _return_405(self, message="Method Not Allowed"):
        """Sends a response with status code 405 - Method Not Allowed"""
        self.send_response(405)
        self._set_headers(len(message))
        self.wfile.write(bytes(message))

    """Define the default answer for all methods"""
    do_GET = _return_405
    do_HEAD = _return_405
    do_POST = _return_405
    do_PUT = _return_405
    do_DELETE = _return_405
    do_CONNECT = _return_405
    do_OPTIONS = _return_405
    do_TRACE = _return_405
    do_PATCH = _return_405


