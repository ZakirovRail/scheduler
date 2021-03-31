import sqlite3
import time
import sys
from migrations import *
from models import Task
from sql_queries import *

"""
This file is used for:
- Creation a new DB during deploying
- Creation a default admin account
- Verification a user during logging in, if it's existing in the DB
- Retrieve data from a DB
"""


class BaseDB:
    def __init__(self, db_file):
        try:
            self.conn = sqlite3.connect(db_file)
        except Exception as e:
            print('print from create_connection', e)
            sys.exit(1)


class DataWork(BaseDB):

    def __init__(self, db_file):
        super().__init__(db_file)

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

    def create_new_task(self, task: Task):
        """
        To add a new task for a current account
        :return:
        """
        local_id = None
        try:
            c = self.conn.cursor()
            c.execute(creat_new_task_command, [task.title, task.short_desc, task.detailed_desc, task.assigned_to,
                                               task.date_creation, task.deadline, task.status])
            local_id = c.fetchone()[0]
            self.conn.commit()
            print(creat_new_task_command)
        except Exception as e:
            print('print from create_new_task', e)
        return local_id

    def show_all_tasks(self):
        """
        the method which will return all existing tasks. For admin account only
        :return:
        """
        list_tasks = []
        try:
            c = self.conn.cursor()
            c.execute(show_all_users_tasks)
            list_tasks = c.fetchall()
        except Exception as e:
            print('print from shoq_all_tasks', e)
        return list_tasks

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

    def select_all_from_users_table(conn, select_all_from_users_table):
        try:
            c = conn.cursor()
            print(select_all_from_users_table)
            return c.execute(select_all_from_users_table)
        except Exception as e:
            print('print from select_all_from_users_table', e)


if __name__ == '__main__':
    CreatDB.creat_users_table(CreatDB.create_connection('scheduler.db'), create_users_table_command)
    CreatDB.create_tasks_table(CreatDB.create_connection('scheduler.db'), create_task_table_command)
    CreatDB.create_admin_account(CreatDB.create_connection('scheduler.db'),
                                 creat_admin_account_command)  # Failed for creating admin account. Why?
    CreatDB.select_all_from_users_table(CreatDB.create_connection('scheduler.db'), select_all_from_users_table)
