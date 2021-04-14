import logging
import sqlite3
import sys
import log_config
import logging

"""
This file is used for:
- Creation a new DB during deploying
- Creation a default admin account
- Verification a user during logging in, if it's existing in the DB
- Retrieve data from a DB
"""

logger = logging.getLogger('scheduler')


class BaseDB:
    def __init__(self, db_file):
        try:
            self.conn = sqlite3.connect(db_file)
            logger.info(f'Connected to DB, connection data -  {self.conn}')
        except Exception as e:
            print('print from create_connection', e)
            logger.critical(f'Exception occurred. Application will be closed. Error - {e}')
            sys.exit(1)


if __name__ == '__main__':
    pass
