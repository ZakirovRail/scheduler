from models_db import User
from utils import encode_password, render_template
import logging
import sys


sys.path.append('../')

logger = logging.getLogger('scheduler')


def authorisation(request):
    return render_template('templates/authorization.html')


def login(request):
    if request['method'] == 'POST':
        current_user = User.get_user_by_login(request['POST']['login'])
        if encode_password(request['POST']['password']) == current_user.password:
            # current_user.is_auth = True
            # TO DO - return to authorised user page (html page for user)
            pass
        print('Method POST')
    elif request['method'] == 'GET':
        print('Method GET')
    return render_template('templates/authorization.html')


def register(request):
    return render_template('templates/registration.html')


if __name__ == '__main__':
    pass
