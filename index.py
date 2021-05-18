from http.server import BaseHTTPRequestHandler, HTTPServer
import time
from jinja2 import Template
import settings
from urls import get_function
from utils import get_static


class SchedulerServer(BaseHTTPRequestHandler):

    def do_GET(self):
        request = {'method': 'GET'}
        # print(self.path)
        self.send_response(200)
        if '/static/' in self.path:
            results = get_static(self.path)
            if '.js' in self.path:
                self.send_header('Content-type', 'text/js')
                self.end_headers()
            elif '.css' in self.path:
                self.send_header('Content-type', 'text/css')
                self.end_headers()
            # here should be processing of images
            else:
                print('Undefined type of file')
        else:
            controller, params = get_function(self.path)
            results = controller(request, *params) # as a HW to envelop in IF controler ELSE
            self.send_header('Content-type', 'text/html')
            self.end_headers()
        self.wfile.write(bytes(results, 'utf-8'))

    def do_POST(self):
        print(self)
        length = int(self.headers['content-length'])
        print('Length is - ', length)
        data = str(self.rfile.read(length), 'utf-8')
        print(data)
        data_list = data.split('&')
        data_dict = {}
        for item in data_list:
            temp = item.split('=')
            print(temp)
            data_dict[temp[0]] = temp[1]
        request = {'method': 'POST', 'POST': data_dict}
        controller, params = get_function(self.path)
        results = controller(request, *params)
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
