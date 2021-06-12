import settings
from models_db import User, UsersSession
from utils import encode_password, render_template, Redirect
import logging
import sys
from ORM import SessionsWork


sys.path.append('../')

logger = logging.getLogger('scheduler')


def authorisation(request):
    return render_template('templates/authorization.html')


def login(request):
    if request['method'] == 'POST':
        current_user = User.get_user_by_login(request['POST']['login'])
        if encode_password(request['POST']['password']) == current_user.password:
            user_session = UsersSession(settings.DB_NAME, current_user)
            request['session'] = user_session.token
            return Redirect('', request)
        print('Method POST')
    elif request['method'] == 'GET':
        print('Method GET')
    return render_template('templates/authorization.html')


def register(request):
    return render_template('templates/registration.html')


# def logout(request):
#     print('User should be logout')
#     print(f'the info inside the "request" parameter - {request}')
#     try:
#         if 'user' in request:
#             print(request['user'])
#             SessionsWork.delete_session(request['user'])
#
#     except Exception as e:
#         logger.error(f'Error happened during logout action - {e!r}')
#         logger.error(f'Error happened during showing all records - {repr(e)}')
#     return render_template('templates/authorization.html')


if __name__ == '__main__':
    pass
