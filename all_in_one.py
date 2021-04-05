import datetime
from abc import ABC
from typing import List
from tabulate import tabulate
import sqlite3
import sys
from sql_queries import create_task_table_command, create_users_table_command, data_seeding_task_command_1, \
    data_seeding_task_command_2, creat_new_task_command, show_all_users_tasks, COLLUMNS, show_all_active_tasks,\
    data_seeding_task_command_3, show_completed_tasks_command, delete_all_tasks_command


class BaseModel(ABC):
    id: int


class Task(BaseModel):
    title: str
    short_desc: str
    detailed_desc: str
    assigned_to: str
    date_creation: datetime
    deadline: datetime
    status: int
    available_statuses = {1: 'New', 2: 'In Progress', 3: 'Closed'}

    def __init__(self, title, short_desc, detailed_desc, deadline, date_creation=datetime.datetime.now(), status=1):
        self.title = title
        self.short_desc = short_desc
        self.detailed_desc = detailed_desc
        self.date_creation = date_creation
        self.deadline = deadline
        self.status = status


class User(BaseModel):
    tasks: List[Task]
    name: str
    short_desc: str
    # db_worker: DataWork

    def __init__(self, db_file):
        self.db_worker = DataWork(db_file)

    def show_all(self):
        all_tasks = self.db_worker.show_all_tasks()
        # columns = ["id", "title", "short_desc", "detailed_desc", "assigned_to", "date_creation", "deadline", "status"]
        columns = ["title", "short_desc", "detailed_desc", "assigned_to", "date_creation", "deadline", "status"]
        for task in all_tasks:
            print(f'Task number: {task["id"]}')
            for column in columns:
                if column in task:
                    print(f'Column name: {column}, column value: {task[column]}')
            # print(f'id: {task["id"]}, title: {title}, short_desc:{short_desc},
            # detailed_desc:{detailed_desc}, assigned_to:{assigned_to},'
            #       f'date_creation:{date_creation}, deadline:{deadline}, status:{status}')
            # print(tabulate(task, headers = columns))

    def create_task(self, conn):
        name = input('Enter a name for a new task: ')
        short_desc = input('Enter a short description for a new task: ')
        detailed_desc = input('Enter a detailed description for a new task: ')
        deadline = input('Enter a deadline for a new task: ')

        new_task = Task(name, short_desc, detailed_desc, deadline)
        new_task.id = self.db_worker.create_new_task(new_task)
        self.tasks.append(new_task)


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
        return print(tabulate(list_tasks, headers=COLLUMNS), '\n')

    def all_active_tasks(conn, show_all_active_tasks, COLLUMNS):
        list_active_tasks = []
        try:
            c = conn.cursor()
            c.execute(show_all_active_tasks)
            list_active_tasks = c.fetchall()
        except Exception as e:
            print('print from show_all_active_tasks', e)
        return print(tabulate(list_active_tasks, headers=COLLUMNS), '\n')

    def show_completed_tasks(conn, show_completed_tasks_command, COLLUMNS):
        list_completed_tasks = []
        try:
            c = conn.cursor()
            c.execute(show_completed_tasks_command)
            list_completed_tasks = c.fetchall()
        except Exception as e:
            print('print from list_completed_tasks', e)
        return print(tabulate(list_completed_tasks, headers=COLLUMNS), '\n')

    def set_status(self, id_task):
        pass

    def delete_all_tasks(conn , delete_all_tasks_command):
        try:
            c = conn.cursor()
            c.execute(delete_all_tasks_command)
            conn.commit()
        except Exception as e:
            print('print from delete_all_tasks', e)
        return print('Deleted all tasks from DB')

    def delete_task(id_task):
        pass


class CreatDB(BaseDB):
    """
    This class for creating a new DB and creating a default admin account
    """
    def __init__(self, db_file):
        super().__init__(db_file)

    def create_tasks_table(conn, create_task_table_command):
        """
        create a new tasks table in the DB SQLite for tasks
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


class DataSeeding(BaseDB):
    """
    This class for data seeding a new DB and creating a default tasks
    """
    def __init__(self, db_file):
        super().__init__(db_file)

    def data_seeding_task(conn, data_seeding_task_command):
        """
        create a new DB SQLite for tasks
        :return:
        """
        try:
            c = conn.cursor()
            c.execute(data_seeding_task_command)
            conn.commit()
        except Exception as e:
            print('print from data_seeding_task_command', e)


if __name__ == '__main__':
    BaseDB('scheduler.db')
    CreatDB.create_tasks_table(BaseDB('scheduler.db').conn, create_task_table_command)
    # CreatDB.creat_users_table(BaseDB('scheduler.db').conn, create_users_table_command)
    DataSeeding.data_seeding_task(BaseDB('scheduler.db').conn, data_seeding_task_command_1)
    DataSeeding.data_seeding_task(BaseDB('scheduler.db').conn, data_seeding_task_command_2)
    DataSeeding.data_seeding_task(BaseDB('scheduler.db').conn, data_seeding_task_command_3)
    DataWork.show_all_tasks(BaseDB('scheduler.db').conn, show_all_users_tasks, COLLUMNS)
    DataWork.all_active_tasks(BaseDB('scheduler.db').conn, show_all_active_tasks, COLLUMNS)
    DataWork.show_completed_tasks(BaseDB('scheduler.db').conn, show_completed_tasks_command, COLLUMNS)
    DataWork.delete_all_tasks(BaseDB('scheduler.db').conn, delete_all_tasks_command)
