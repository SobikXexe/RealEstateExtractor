import argparse
from http.server import HTTPServer, BaseHTTPRequestHandler
import html_generator as hg

class HTTPHandler(BaseHTTPRequestHandler):

    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write(hg.render_page().encode("utf8"))


def run(addr, port):
    server_address = (addr, port)
    httpd = HTTPServer(server_address, HTTPHandler)

    print("Starting http server on " + str(addr) + ":" + str(port))
    httpd.serve_forever()


if __name__ == "__main__":

    run(addr="0.0.0.0", port=8080)