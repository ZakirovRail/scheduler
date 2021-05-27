from ORM import DataWork
from sql_queries import create_task_table_command, create_users_table_command, create_users_session_table_command,\
    creat_admin_account_command, \
    data_seeding_task_command_1, data_seeding_task_command_2, data_seeding_task_command_3, data_seeding_user_command_1,\
    data_seeding_user_command_2, data_seeding_user_command_3

from db_main_com import BaseDB
from models_db import UsersSession
import settings
import logging
from utils import encode_password
import time

logger = logging.getLogger('scheduler')


class CreatDB(BaseDB):
    """
    This class for creating a new DB and creating a default admin account
    """
    def __init__(self, db_file):
        super().__init__(db_file)

    def create_tasks_table(self):
        """
        create a new tasks table in the DB SQLite for tasks
        :return:
        """
        try:
            c = self.conn.cursor()
            c.execute(create_task_table_command)
            logger.debug(f'The "Task" table were created')
        except Exception as e:
            logger.critical(f'The "Task" table WAS NOT created, the following error happened - {str(e)}')
            logger.critical(f'The "Task" table WAS NOT created, the following error happened - {repr(e)}')

    def creat_users_table(self):
        """
        create a new DB SQLite for users
        :return:
        """
        try:
            c = self.conn.cursor()
            c.execute(create_users_table_command)
            logger.debug(f'The "Users" table were created')
        except Exception as e:
            logger.critical(f'The "Users" table WAS NOT created, the following error happened - {e}')
            print('print from creat_users_table', e)

    def create_user_session_table(self):
        """
        create a new DB SQLite for users session
        :return:
        """
        try:
            c = self.conn.cursor()
            c.execute(create_users_session_table_command)
            logger.debug(f'The "Users session" table were created')
        except Exception as e:
            logger.critical(f'The "Users session" table WAS NOT created, the following error happened - {e}')
            print('print from creat_users_table', e)

    def create_admin_account(self):
        """
        create a default admin account during deploying a new DB
        :return:
        """
        try:
            c = self.conn.cursor()
            c.execute(creat_admin_account_command)
            logger.debug(f'The "Admin" table were created')
        except Exception as e:
            logger.critical(f'The "Admin" table WAS NOT created, the following error happened - {e}')
            print('print from create_admin_account', e)


class DataSeeding(BaseDB):
    """
    This class for data seeding a new DB and creating a default tasks
    """
    def __init__(self, db_file):
        super().__init__(db_file)

    def data_seeding_tasks(self):
        """
        to fill a table "tasks" with a test data
        """
        try:
            c = self.conn.cursor()
            c.execute(data_seeding_task_command_1)
            c.execute(data_seeding_task_command_2)
            c.execute(data_seeding_task_command_3)
            self.conn.commit()
            logger.debug(f'Data seeding for the "Tasks" table were done')
        except Exception as e:
            logger.critical('Failed data seeding, error print from create_tasks_table', e)

    def data_seeding_users(self):
        """
        to fill a table "users" with a test data
        """
        user_name = 'John'
        user_surname = 'Connor'
        reg_date = '1985-01-01'
        hex_pass = encode_password('Secret')
        users_data = (user_name, user_surname, hex_pass, reg_date)
        try:
            c = self.conn.cursor()
            c.execute(data_seeding_user_command_1)
            c.execute(data_seeding_user_command_2)
            c.execute(data_seeding_user_command_3)
            c.execute("INSERT into users (user_name, user_surname, password, reg_date) VALUES (?,?,?,?)", (users_data))
            self.conn.commit()
            logger.debug(f'Data seeding for the "Users" table were done')
        except Exception as e:
            logger.critical('Failed data seeding for users table, error print from create_tasks_table', e)

    def data_seeding_sessions(self):
        user = 4
        auth_date = time.time()
        expires_time = auth_date + settings.SESSION_LIVE
        token = UsersSession.gen_session_token(self)
        data_to_seed = (user, auth_date, expires_time, token)
        logger.debug(f'The following test data for sessions will be tried to seed to DB: {data_to_seed} ')
        try:
            c = self.conn.cursor()
            c.execute("INSERT into users_session (user, auth_date, expires_date, token) VALUES (?,?,?,?)", (data_to_seed))
            self.conn.commit()
            logger.debug(f'Data seeding for the "Users" table were done')
        except Exception as e:
            logger.critical('Failed data seeding for users_sessions table. ', e)


if __name__ == '__main__':
    create_db = CreatDB(settings.DB_NAME)
    create_db.create_tasks_table()
    create_db.creat_users_table()
    create_db.create_user_session_table()

    seeding = DataSeeding(settings.DB_NAME)
    seeding.data_seeding_tasks()
    seeding.data_seeding_users()
    seeding.data_seeding_sessions()


    # work_data = DataWork(settings.DB_NAME)
    # work_data.show_info(1)
    # work_data.show_all_tasks()
    # work_data.all_active_tasks()
    # work_data.show_completed_tasks()
    # work_data.delete_all_tasks()
