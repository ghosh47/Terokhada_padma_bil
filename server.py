import os
import sys
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler

PORT = 3000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class FastHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_GET(self):
        if self.path.startswith('/log?'):
            import urllib.parse
            query = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
            msg = query.get('msg', [''])[0]
            print(f"[CLIENT LOG] {msg}")
            sys.stdout.flush()
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'ok')
            return
        super().do_GET()

    def end_headers(self):
        if self.path.endswith('.jpg') or self.path.endswith('.jpeg'):
            self.send_header('Cache-Control', 'public, max-age=31536000, immutable')
        else:
            self.send_header('Cache-Control', 'no-cache')
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

    def log_message(self, format, *args):
        if args and any(str(a).startswith('200') or str(a).startswith('304') for a in args):
            return
        super().log_message(format, *args)

def run():
    port = PORT
    server_address = ('0.0.0.0', port)
    try:
        httpd = ThreadingHTTPServer(server_address, FastHandler)
        print(f"Serving at http://localhost:{port}/ and http://127.0.0.1:{port}/")
        sys.stdout.flush()
        httpd.serve_forever()
    except OSError:
        port = 8080
        server_address = ('0.0.0.0', port)
        httpd = ThreadingHTTPServer(server_address, FastHandler)
        print(f"Serving at http://localhost:{port}/ and http://127.0.0.1:{port}/")
        sys.stdout.flush()
        httpd.serve_forever()

if __name__ == '__main__':
    run()
