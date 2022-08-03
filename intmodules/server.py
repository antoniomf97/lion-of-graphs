import socketserver
from http.server import SimpleHTTPRequestHandler
from http.server import HTTPServer


class Response:
    def __init__(self, status_code: int, message: str, content: str):
        self.status_code = status_code
        self.message = message
        self.content = content


class MPBServerHandler(SimpleHTTPRequestHandler):
    def __init__(self, service, request: bytes, client_address: (str, int), server: socketserver.BaseServer):
        super().__init__(request, client_address, server)
        self.service = service

    def _set_headers(self, content_length):
        self.send_header('Content-type', 'text/html')
        self.send_header("Content-Length", content_length)
        self.end_headers()

    def do_GET(self):
        self.send_response(405)
        self._set_headers("0")

    def do_POST(self):
        content_length = int(self.headers.get("content-length", "0"))
        length = int(content_length) if content_length else 0
        request = self.rfile.read(length)

        response = self.service(request)

        match response.status_code:
            case 200:
                self.send_response(response.status_code)
                self._set_headers(str(len(response.content)))
                self.wfile.write(response.content)
            case 400:
                pass
            case 500:
                pass

    do_PUT = do_POST
    do_DELETE = do_GET
