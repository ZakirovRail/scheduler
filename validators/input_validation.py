from settings import SYMBOLS
import re
from actions import tasks, users
import sys
import logging

logger = logging.getLogger('scheduler')
sys.path.append('../')


def not_empty_input(users_input):
    if len(users_input) == 0:
        return 'You entered an empty string, please repeat your attempt'


def len_password(users_password):
    """
    password should have a length from 8 to 15 symbols
    """
    if len(users_password) != 8:
        return 'You should enter a password 8 characters long'


def spec_char_password(users_password):
    """
    password should have a special characters
    """
    pass


def digits_char_password(users_password):
    """
    password should have a digits
    """
    pass
