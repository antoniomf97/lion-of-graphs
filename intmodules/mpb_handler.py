from http.server import SimpleHTTPRequestHandler

class MpbHandler(SimpleHTTPRequestHandler):
    # define private methods for the most common returns with defaults
    # except the 200 -> that one should always be 100% handled by the actual
    # service handler class
    def _return_201(self):
        self.send_response(201)
        self.send_header('Content-Length', '0')
        self.end_headers()
        
    # ...

    def _return_405(self, msg = 'Method is not allowed in this service'):
        self.send_response(405)
        self.send_header('Content-type', 'text/plain')
        self.send_header('Content-Length', str(len(msg)))
        self.end_headers()
        self.wfile.write(msg)

    # ...

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


