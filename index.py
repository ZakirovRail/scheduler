from http.server import BaseHTTPRequestHandler, HTTPServer
from http import cookies
import time
from idlelib.pyshell import HOST

from jinja2 import Template
import settings
from models_db import UsersSession
from urls import get_function
from utils import get_static, Redirect
import logging

logger = logging.getLogger('scheduler')


class SchedulerServer(BaseHTTPRequestHandler):
    # C = cookies.SimpleCookie()

    def do_GET(self):
        logger.debug(f'The self for do_GET method - {self}')
        request = {'method': 'GET'}
        # print(self.path)
        if '/static/' in self.path:
            results = get_static(self.path)
            if results is None:
                self.send_response(404)
                results = '<H1>404</H1>'
            else:
                self.send_response(200)
                if '.js' in self.path:
                    self.send_header('Content-type', 'text/js')
                    # self.send_header('Cookies', '')
                    self.end_headers()
                elif '.css' in self.path:
                    self.send_header('Content-type', 'text/css')
                    # self.send_header('Cookies', '')
                    self.end_headers()
                elif '.ico' in self.path:
                    self.send_header('Content-type', 'image/x-icon')
                    self.end_headers()
                else:
                    logger.warning(f'Undefined type of file in path - {self.path}')
            self.wfile.write(bytes(results, 'utf-8'))
        else:
            cookie = cookies.SimpleCookie(self.headers.get('Cookie'))
            token_value = ''
            if 'user-token' in cookie:
                token_value = cookie['user-token'].value
                user = UsersSession.get_by_token(token_value)  # In get_by_token надо получить или пользователя или None -
                if user:
                    request['user'] = user
            # there is no ELSE block, because if no else, that means we have an unanimous user
            controller, params = get_function(self.path)
            logger.debug(f'The controller is  - {controller}')
            logger.debug(f'The params is  - {params}')
            try:
                if controller is None:
                    self.send_response(404)
                    results = '<H1>404</H1>'
                else:
                    if len(params) == 0:
                        results = controller(request)
                    else:
                        results = controller(request, *params)
                    if isinstance(results, Redirect):
                        self.send_response(301)
                        self.send_header('Location', f'http://{settings.HOST_NAME}:{settings.HOST_PORT}/{results.path}')
                    else:
                        self.send_response(200)
                cookie = cookies.SimpleCookie()
                cookie['user-token'] = token_value
                for morsel in cookie.values():
                    self.send_header("Set-Cookie", morsel.OutputString())
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(bytes(results, 'utf-8'))
            except Exception as ex:
                logger.error(
                    f'The request will be sent with GET request with following parameters:controller-{controller}'
                    f'params - {ex}')
        logger.debug('The HTML successfully will be sent with GET request')

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
        cookie = cookies.SimpleCookie(self.headers.get('Cookie'))  # move to utils file
        if 'user-token' in cookie:
            token_value = cookie['user-token'].value
            user = UsersSession.get_by_token(token_value)  # In get_by_token надо получить или пользователя или None -
            if user:
                request['user'] = user
        controller, params = get_function(self.path)
        logger.debug(f'The following params will be sent with POST request: controller - {controller} and '
                     f'params - {params}')
        results = controller(request, *params)
        if isinstance(results, Redirect):
            self.send_response(301)
            cookie = cookies.SimpleCookie()
            cookie['user-token'] = results.request['session']
            for morsel in cookie.values():
                self.send_header("Set-Cookie", morsel.OutputString())
            self.send_header('Location', f'http://{settings.HOST_NAME}:{settings.HOST_PORT}/{results.path}')
            self.end_headers()
        else:
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            # self.send_header('Cookies', '')
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
