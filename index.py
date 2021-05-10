from http.server import BaseHTTPRequestHandler, HTTPServer
import time
from jinja2 import Template
import settings
from urls import get_function


class SchedulerServer(BaseHTTPRequestHandler):

    def do_GET(self):
        controller, params = get_function(self.path)
        print(self.path)
        print(params)
        results = controller(*params)
        with open('templates/index.html', 'r') as f:
            index_main = f.read()
        template = Template(index_main)
        render_template = template.render(path=self.path)
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes(results, 'utf-8'))


if __name__ == '__main__':
    web_server = HTTPServer((settings.HOST_NAME, settings.HOST_PORT), SchedulerServer)
    try:
        web_server.serve_forever()
    except KeyboardInterrupt:
        pass
    web_server.server_close()
