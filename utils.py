import time
import codecs
import os.path
import sys
import hashlib
import logging
from jinja2 import Template, BaseLoader, Environment, FileSystemLoader

logger = logging.getLogger('scheduler')


def exit_program():
    print('You selected to exit from the program. Thank you.')
    logger.debug(f'The user selected EXIT.')
    sys.exit(0)


def encode_password(password):
    if len(password) != 0:
        try:
            hash_alg = hashlib.sha256()
            encoded_password = password.encode()
            hash_alg.update(encoded_password)
            hex_pass = hash_alg.hexdigest()
            logger.debug(f'The password will be encrypted to - {hex_pass}')
            return hex_pass
        except Exception as e:
            logger.critical('Failed password encrypting', e)
    else:
        return 'The length of the password is 0, you should enter a password'


def render_template(template, context={}):
    with open(template, 'r') as f:
        template_contain = f.read()
    # template = Template(template_contain)
    # return template.render(**context)
    # rtemplate = Environment(loader=BaseLoader).from_string(template_contain)
    # data = rtemplate.render(**context)
    template = Environment(loader=FileSystemLoader("templates/")).from_string(template_contain)
    html_str = template.render(**context)
    return html_str


def get_static(path: str):
    if os.path.exists(path[1:]):
        with codecs.open(path[1:], 'r', encoding='UTF-8', errors='ignore') as static_file:
            read_static_file = static_file.read()
        return read_static_file
    else:
        return None


class Redirect:
    def __init__(self, path, request):
        self.path = path
        self.request = request
