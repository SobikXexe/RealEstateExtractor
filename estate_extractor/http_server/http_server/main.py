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
    print(f"Starting http server on {addr}:{port}")
    httpd.serve_forever()


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-l",
        "--listen",
        default="localhost",
        help="Specify the IP address on which the server listens. Default is localhost.",
    )
    parser.add_argument(
        "-p",
        "--port",
        type=int,
        default=9090,
        help="Specify the port on which the server listens. Default is 9090.",
    )
    args = parser.parse_args()
    run(addr=args.listen, port=args.port)