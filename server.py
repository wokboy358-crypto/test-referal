import http.server, os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

class H(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith('/ref/'):
            self.path = '/index.html'
        super().do_GET()

print('http://localhost:8000')
http.server.ThreadingHTTPServer(('', 8000), H).serve_forever()
