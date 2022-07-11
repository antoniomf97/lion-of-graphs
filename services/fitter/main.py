#!/usr/bin/env python3

from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

class FitterHandler(SimpleHTTPRequestHandler):
    def _set_headers(self, content_length):
        self.send_header('Content-type', 'text/html')
        self.send_header("Content-Length", content_length)
        self.end_headers()

        
    def do_GET(self):
        self.send_response(400)
        self._set_headers("0")

    def do_POST(self):
        content_length = self.headers['content-length']
        length = int(content_length[0]) if content_length else 0
        
        data_string = self.rfile.read(length)

        self.send_response(200)
        self._set_headers(str(len(data_string)))
        self.wfile.write(data_string)
    
    do_PUT = do_POST
    do_DELETE = do_GET


httpd = TCPServer(('', 8000), FitterHandler)

httpd.serve_forever()