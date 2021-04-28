import sys
from models_db import User
from utils import encode_password
import logging

logger = logging.getLogger('scheduler')


def authorisation():
    user_first_action = input('Hello, do you want to register yourself or you want to login?'
                            ' Enter to "login" or "register": ')
    if user_first_action == "login":
        current_user = login()
    elif user_first_action == "register":
        current_user = register()
    else:
        print('You entered a wrong option, buy')
        sys.exit(1)
    return current_user


def login():
    while True:
        login_name = str(input('Enter your login: '))
        current_user = User.get_user_by_login(login_name)
        if current_user is not None:
            for _ in range(3):
                password = (input('Enter your password: '))
                if encode_password(password) == current_user.password:
                    current_user.is_auth = True
                    break
                else:
                    print('You entered a wrong password. Try again')
        if current_user is None or not current_user.is_auth:
            print('User is not defined, the session will be closed')
            sys.exit(1)
        else:
            print(f'Welcome {current_user.user_name} to the System')
            break
    return current_user


def register():
    while True:
        name = str(input('Enter your name: '))
        if User.get_user_by_login(name) is None:
            surname = str(input('Enter your surname: '))
            password = str(input('Enter your password: '))
            new_current_user = User.create_new_user(name, surname, password)
            new_current_user.is_auth = True
            return new_current_user
        else:
            variant = input('Entered user name is existing, you can login - [y/n]: ')
            if variant == 'y':
                return login()
            elif variant == 'n':
                print('You selected to cancel authorisation.')
                continue


if __name__ == '__main__':
    pass
