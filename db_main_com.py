import sqlite3
import sys
# from migrations import *
from models_db import BaseModel, Task, User
from sql_queries import create_task_table_command, create_users_table_command, data_seeding_task_command_1, \
    data_seeding_task_command_2, creat_new_task_command, show_all_users_tasks, COLLUMNS, show_all_active_tasks,\
    data_seeding_task_command_3, show_completed_tasks_command, delete_all_tasks_command
from tabulate import tabulate

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


    def show_info(self, id_task):
    #     """
    #     get an information about current tasks for a logged user
    #     :return:
    #     """
    #     id_task = id_task
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

    def show_all_tasks(conn, show_all_users_tasks, COLLUMNS):
        """
        the method which will return all existing tasks. For admin account only
        :return:
        """
        list_tasks = []
        try:
            c = conn.cursor()
            c.execute(show_all_users_tasks)
            list_tasks = c.fetchall()
        except Exception as e:
            print('print from show_all_tasks', e)
        return print(tabulate(list_tasks, headers=COLLUMNS))

    def all_active_tasks(conn, show_all_active_tasks, COLLUMNS):
        list_active_tasks = []
        try:
            c = conn.cursor()
            c.execute(show_all_active_tasks)
            list_active_tasks = c.fetchall()
        except Exception as e:
            print('print from all_active_tasks', e)
        return print(tabulate(list_active_tasks, headers=COLLUMNS), '\n')

    def show_completed_tasks(conn, show_completed_tasks_command, COLLUMNS):
        list_completed_tasks = []
        try:
            c = conn.cursor()
            c.execute(show_completed_tasks_command)
            list_completed_tasks = c.fetchall()
        except Exception as e:
            print('print from show_completed_tasks', e)
        return print(tabulate(list_completed_tasks, headers=COLLUMNS), '\n')

    def set_status(self, id_task):
        pass

    def delete_all_tasks(conn, delete_all_tasks_command):
        try:
            c = conn.cursor()
            c.execute(delete_all_tasks_command)
            conn.commit()
        except Exception as e:
            print('print from delete_all_tasks', e)
        return print('Deleted all tasks from DB')

    def delete_task(id_task):
        pass


if __name__ == '__main__':
    BaseDB('scheduler.db')
    # CreatDB.create_tasks_table(BaseDB('scheduler.db').conn, create_task_table_command)
    # CreatDB.creat_users_table(BaseDB('scheduler.db').conn, create_users_table_command)
    # DataSeeding.data_seeding_task(BaseDB('scheduler.db').conn, data_seeding_task_command_1)
    # DataSeeding.data_seeding_task(BaseDB('scheduler.db').conn, data_seeding_task_command_2)
    # DataSeeding.data_seeding_task(BaseDB('scheduler.db').conn, data_seeding_task_command_3)
    # DataWork.show_all_tasks(BaseDB('scheduler.db').conn, show_all_users_tasks, COLLUMNS)
    # DataWork.all_active_tasks(BaseDB('scheduler.db').conn, show_all_active_tasks, COLLUMNS)
    # DataWork.show_completed_tasks(BaseDB('scheduler.db').conn, show_completed_tasks_command, COLLUMNS)
    # DataWork.delete_all_tasks(BaseDB('scheduler.db').conn, delete_all_tasks_command)


