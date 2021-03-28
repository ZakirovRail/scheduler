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
        Get the information about all accaunts in the DB. For admin account only
        :return:
        """
        pass

    def show_info(id_task):
        """
        get an information about current tasks for a logged user
        :return:
        """
        id_task = id_task
        pass

    def create_new_task(self):
        """
        To add a new task for a current account
        :return:
        """
        pass

    def check_login(self, login_name, password):
        """
        the method to check if login name presents in the DB
        :return:
        """
        pass

    def show_all_user(self, user_name):
        """
        the method which will return all existing tasks for a user
        :return:
        """
        pass

    def show_all_tasks_admin(self):
        """
        the method which will return all existing tasks. For admin account only
        :return:
        """
        pass

    def all_active_for_admin(self):
        pass

    def all_active_for_user(self):
        pass

    def show_completed_for_all(self):
        pass

    def show_completed_user(self):
        pass

    def set_status_admin(self, id_task):
        pass

    def set_status_user(self, id_task):
        pass

    def delete_all_tasks(self):
        pass

    def delete_task(id_task):
        pass

    def assign_task(self, id_task, id_user):
        pass


if __name__ == '__main__':
    CreatDB.creat_users_table(CreatDB.create_connection('scheduler.db'), create_users_table_command)
    CreatDB.create_tasks_table(CreatDB.create_connection('scheduler.db'), create_task_table_command)
    CreatDB.create_admin_account(CreatDB.create_connection('scheduler.db'), creat_admin_account_command)  # Failed for creating admin account. Why?
    CreatDB.select_all_from_users_table(CreatDB.create_connection('scheduler.db'), select_all_from_users_table)
