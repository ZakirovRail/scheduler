import sqlite3
import time
"""
This file is used for:
- Creation a new DB during deploying
- Creation a default admin account
- Verification a user during logging in, if it's existing in the DB
- Retrieve data from a DB
"""

create_task_table_command = """CREATE TABLE IF NOT EXISTS tasks (
	id integer PRIMARY KEY,
	task_name text NOT NULL,
    priority text,
    short_desc text,
	deadline_date text,
	repons text
);"""

create_users_table_command = """
        CREATE TABLE IF NOT EXISTS users (
	id integer PRIMARY KEY AUTOINCREMENT,
	user_name text NOT NULL,
	user_surname text NOT NULL,
	password text NOT NULL,
	reg_date text
);
"""

creat_admin_account_command = """
    INSERT INTO users(user_name, user_surname, password, reg_date)
    VALUES ('Mainaccount', 'Mainaccount', 'Mainpassword', datetime('now'));
"""

select_all_from_users_table = """
    SELECT * FROM users;
"""


class CreatDB:
    """
    This class for creating a new DB and creating a default admin account
    """
    def __init__(self):
        pass

    def create_connection(db_file):
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Exception as e:
            print('print from create_connection', e)
        return conn

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

    def select_all_from_users_table(conn, select_all_from_users_table):
        try:
            c = conn.cursor()
            print(select_all_from_users_table)
            return c.execute(select_all_from_users_table)
        except Exception as e:
            print('print from select_all_from_users_table', e)


class DataWork:
    def get_accounts_info(self):
        """
        for admin account only
        :return:
        """
        pass

    def get_tasks_info(self):
        """
        get an information about current tasks for a logged user
        :return:
        """
        pass

    def add_new_task(self):
        """
        To add a new task for a current account
        :return:
        """
        pass


if __name__ == '__main__':
    CreatDB.creat_users_table(CreatDB.create_connection('scheduler.db'), create_users_table_command)
    CreatDB.create_tasks_table(CreatDB.create_connection('scheduler.db'), create_task_table_command)
    CreatDB.create_admin_account(CreatDB.create_connection('scheduler.db'), creat_admin_account_command)  # Failed for creating admin account. Why?
    CreatDB.select_all_from_users_table(CreatDB.create_connection('scheduler.db'), select_all_from_users_table)
