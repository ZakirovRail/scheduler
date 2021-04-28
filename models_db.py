import datetime
from abc import ABC
from typing import List

import settings
from ORM import DataWork
from tabulate import tabulate
from db_main_com import BaseDB
import logging
from sql_queries import COLLUMNS
from settings import DB_NAME
import utils

logger = logging.getLogger('scheduler')


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

    # def __init__(self, title, short_desc, detailed_desc, deadline, date_creation=datetime.datetime.now(), status=1):
    #     self.title = title
    #     self.short_desc = short_desc
    #     self.detailed_desc = detailed_desc
    #     self.date_creation = date_creation
    #     self.deadline = deadline
    #     self.status = status

    def request_task_data(self):
        print('Please enter the following info for a new task: ')
        self.title = input("Please enter the tasks name: ")
        self.short_desc = input("Please enter the tasks short description: ")
        self.detailed_desc = input("Please enter the tasks detailed description: ")
        task_deadline = input("Please enter the deadline for the task (dd.mm.yyyy): ")
        while True:
            try:
                self.deadline = datetime.datetime.strptime(task_deadline, "%d.%m.%Y")
                logger.debug(f'The following data for a task received: /n'
                             f'title - {self.title}/n'
                             f'Short description - {self.short_desc}/n'
                             f'Detailed description - {self.detailed_desc}/n'
                             f'Deadline - {task_deadline}/n')
                break
            except Exception as e:
                logger.critical(f'The wrong format for data were entered ({task_deadline})')
                task_deadline = input('Please enter a correct format of data, which is  - dd.mm.yyyy')
        self.date_creation = datetime.datetime.now()
        self.status = 1

    @staticmethod
    def print_tasks(list_tasks):
        print(tabulate(list_tasks, headers=COLLUMNS))
        for task_item in list_tasks:
            task_item.print_one_task()

    def print_one_task(self, is_short_view=True):
        if is_short_view:
            print(f'The id of the task is: {self.id}')
            print(f'The title of the task is: {self.title}')
            print(f'The short description of the task is: {self.short_desc}')
            print(f'The task is assigned to: {self.assigned_to}')
            print(f'The status of the task is: {self.available_statuses[self.status]}')
        else:
            print(f'The id of the task is: {self.id}')
            print(f'The title of the task is: {self.title}')
            print(f'The short description of the task is: {self.short_desc}')
            print(f'The detailed description of the task is: {self.detailed_desc}')
            print(f'The task is assigned to: {self.assigned_to}')
            print(f'The date of creation of the task is: {self.date_creation.strftime("%d.%m.%Y")}')
            print(f'The deadline of the task is: {self.deadline.strftime("%d.%m.%Y")}')
            print(f'The status of the task is: {self.available_statuses[self.status]}')


class User(BaseModel):
    id: int
    user_name: str
    user_surname: str
    password: str
    reg_date: str
    tasks: List[Task]
    db_worker: DataWork
    is_auth: bool

    def __init__(self, db_file):
        self.db_worker = DataWork(db_file)
        logger.debug(f'The self.db_worker were initialized as: {db_file}')

    def make_user_object(self, id, user_name, user_surname, password, reg_date):
        self.id = id
        self.user_name = user_name
        self.user_surname = user_surname
        self.password = password
        self.reg_date = reg_date
        self.is_auth = False

    @staticmethod
    def list_active_users():
        db_worker = DataWork(DB_NAME)
        try:
            c = db_worker.conn.cursor()
            c.execute("SELECT * FROM users where id=(?)", (task_id, ))
            task_info = c.fetchall()
            logger.debug(f'The data from DB for active users is following: /n'
                         f'{task_info}')
        except Exception as e:
            logger.critical('print from show_info', e)
        return print(tabulate(task_info, headers=COLLUMNS), '\n')

    @staticmethod
    def get_user_by_login(login_name):
        db_worker = DataWork(DB_NAME)
        try:
            c = db_worker.conn.cursor()
            c.execute("Select * from users where user_name=(?);", (login_name, ))
            login_info = c.fetchone()
            logger.debug(f'The login selected from DB: {login_info}')
            # print(type(login_info))
            # print(login_info)
        except Exception as e:
            logger.critical('Error during getting login from DB', e)
            return None
        else:
            if login_info is not None:
                return User.serialise_user_data(login_info)
            else:
                logging.debug(f'Wrong user name - {login_name}')
                return None

    @staticmethod
    def serialise_user_data(login_info):
        COLUMNS = ['id', 'user_name', 'user_surname', 'password', 'reg_date']
        user_dict_name = dict(zip(COLUMNS, login_info))
        logger.debug(f'The user_dict_name: {user_dict_name}')
        user_object = User(settings.DB_NAME)
        user_object.make_user_object(**user_dict_name)
        # print(user_object.__dict__)
        return user_object

    # def is_authorised(self):
    #     if self.is_auth is None:
    #         return False
    #     else:
    #         return self.is_auth

    def show_all(self):
        all_tasks = self.db_worker.show_all_tasks()
        # columns = ["id", "title", "short_desc", "detailed_desc", "assigned_to", "date_creation", "deadline", "status"]
        columns = ["title", "short_desc", "detailed_desc", "assigned_to", "date_creation", "deadline", "status"]
        logger.debug(f'The list of all task is following: {all_tasks}')
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
        logger.debug(f'The task will be added: {new_task}')
        self.tasks.append(new_task)

    @staticmethod
    def create_new_user(name, surname, password):
        user = User(settings.DB_NAME)
        users_data = (name, surname, utils.encode_password(password), datetime.datetime.now())
        c = user.db_worker.conn.cursor()
        c.execute("INSERT into users (user_name, user_surname, password, reg_date) VALUES (?,?,?,?)", users_data)
        user.db_worker.conn.commit()
        new_user = User.get_user_by_login(name)
        return new_user


if __name__ == '__main__':
    User.get_user_by_login('John')
    User.create_new_user('Mike2', 'Surface2', 'Secret3')

