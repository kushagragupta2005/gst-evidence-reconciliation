"""Serve the static site locally, with a bounded same-origin API bridge.

The bridge adds no database credentials or query logic. An unavailable local
API returns a normal Snapshot response, so optional Live detection is quiet.
"""
import json
import urllib.error
import urllib.request
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]


class Handler(SimpleHTTPRequestHandler):
    def api(self):
        path = self.path.removeprefix('/api')
        allowed = path.split('?', 1)[0]
        if allowed not in {'/health', '/queue', '/ask', '/activity'} and not any(
                allowed.startswith(prefix) for prefix in ('/case/', '/note/')):
            self.send_error(404)
            return
        length = int(self.headers.get('Content-Length', '0'))
        if length > 2048:
            self.send_error(400)
            return
        body = self.rfile.read(length) if self.command == 'POST' else None
        try:
            request = urllib.request.Request('http://127.0.0.1:8765' + path, data=body,
                method=self.command, headers={'Content-Type': 'application/json'})
            with urllib.request.urlopen(request, timeout=1.4 if allowed == '/health' else 31) as response:
                payload = response.read()
        except (OSError, urllib.error.URLError):
            payload = json.dumps({'mode': 'Snapshot', 'available': False}).encode()
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Cache-Control', 'no-store')
        self.send_header('Content-Length', str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def do_GET(self):
        if urlsplit(self.path).path.startswith('/api/'):
            return self.api()
        super().do_GET()

    def do_POST(self):
        if urlsplit(self.path).path.startswith('/api/'):
            return self.api()
        self.send_error(405)


if __name__ == '__main__':
    server = ThreadingHTTPServer(('127.0.0.1', 8081), partial(Handler, directory=str(ROOT / 'website')))
    print('GST Evidence site: http://127.0.0.1:8081', flush=True)
    server.serve_forever()
