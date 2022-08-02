import socketserver
from http.server import SimpleHTTPRequestHandler
from http.server import HTTPServer


class MPBServerHandler(SimpleHTTPRequestHandler):
    def __init__(self, request: bytes, client_address: (str, int), server: socketserver.BaseServer):
        super().__init__(request, client_address, server)
