import sqlite3
from sql_queries import *
from db_main import BaseDB


class CreatDB(BaseDB):
    """
    This class for creating a new DB and creating a default admin account
    """
    def __init__(self, db_file):
        super().__init__(db_file)

    def create_tasks_table(conn, create_task_table_command):
        """
        create a new DB SQLite for tasks
        :return:
        """
        try:
            c = conn.cursor()
            c.execute(create_task_table_command)
        except Exception as e:
            print('print from create_tasks_table', e)

    def creat_users_table(conn, create_users_table_command):
        """
        create a new DB SQLite for users
        :return:
        """
        try:
            c = conn.cursor()
            c.execute(create_users_table_command)
        except Exception as e:
            print('print from creat_users_table', e)

    def create_admin_account(conn, creat_admin_account_command):
        """
        create a default admin account during deploying a new DB
        :return:
        """
        try:
            c = conn.cursor()
            c.execute(creat_admin_account_command)
            print(creat_admin_account_command)
        except Exception as e:
            print('print from create_admin_account', e)