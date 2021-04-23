import time
from db_main import DataWork
import sys

logger = logging.getLogger('scheduler')

# def authorisation(login_name, password):
#     return True  # temporally is set True
#     # DataWork.check_login(login_name, password)
#     pass


# def admin_or_user(login_name):
#     """
#     return admin or user rights
#     :param login_name:
#     :return:
#     """
#     return 'user'


def exit_program():
    print('You selected to exit from the program. Thank you.')
    logger.debug(f'The user selected EXIT.')
    sys.exit(0)


