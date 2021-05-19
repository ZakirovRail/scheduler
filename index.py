from http.server import BaseHTTPRequestHandler, HTTPServer
import time
from jinja2 import Template
import settings
from urls import get_function
from utils import get_static
import logging

logger = logging.getLogger('scheduler')


class SchedulerServer(BaseHTTPRequestHandler):

    def do_GET(self):
        logger.debug(f'The self for do_GET method - {self}')
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
                logger.warning(f'Undefined type of file in path - {self.path}')
        else:
            controller, params = get_function(self.path)
            results = controller(request, *params)  # as a HW to envelop in IF controler ELSE
            logger.debug(f'The request will be sent with GET request with following parameters:controller-{controller}'
                         f'params - {params}')
            self.send_header('Content-type', 'text/html')
            self.end_headers()
        logger.debug(f'The results will be sent with GET request - {results}')
        self.wfile.write(bytes(results, 'utf-8'))

    def do_POST(self):
        logger.debug(f'The self for do_POST method - {self}')
        length = int(self.headers['content-length'])
        logger.debug(f'Length is - {length}')
        data = str(self.rfile.read(length), 'utf-8')
        logger.debug(f'A data for POST request - {data}')
        data_list = data.split('&')
        logger.debug(f'A data_list after splitting for POST request - {data_list}')
        data_dict = {}
        for item in data_list:
            temp = item.split('=')
            data_dict[temp[0]] = temp[1]
        request = {'method': 'POST', 'POST': data_dict}
        logger.debug(f'The POST request is prepared - {request}')
        controller, params = get_function(self.path)
        logger.debug(f'The following params will be sent with POST request: controller - {controller} and '
                     f'params - {params}')
        results = controller(request, *params)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes(results, 'utf-8'))
        logger.debug(f'The POST request is sent with headers')


if __name__ == '__main__':
    web_server = HTTPServer((settings.HOST_NAME, settings.HOST_PORT), SchedulerServer)
    try:
        web_server.serve_forever()
        logger.debug(f'A web server is run with parameters -HOST_NAME{settings.HOST_NAME} '
                     f'and HOST_PORT - {settings.HOST_PORT}')
    except KeyboardInterrupt as e:
        logger.critical('An exception happened during running web server with parameters - '
                        f'HOST_NAME{settings.HOST_NAME} and HOST_PORT - {settings.HOST_PORT}', e)
        pass
    web_server.server_close()
