"""
Task contains:
- Name/Title
- Short description
- Detailed description
- Assigned to
- Date of creation
- Deadline
- Status
"""
import datetime
from abc import ABC
from typing import List

from db_main import DataWork

from tabulate import tabulate


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
    db_worker: DataWork

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
            # print(f'id: {task["id"]}, title: {title}, short_desc:{short_desc}, detailed_desc:{detailed_desc}, assigned_to:{assigned_to},'
            #       f'date_creation:{date_creation}, deadline:{deadline}, status:{status}')
            # print(tabulate(task, headers = columns))


    def show_completed(self):
        pass

    def show_active(self):
        pass

    def show_task(self):
        pass

    def create_task(self, conn):
        name = input('Enter a name for a new task: ')
        short_desc = input('Enter a short description for a new task: ')
        detailed_desc = input('Enter a detailed description for a new task: ')
        deadline = input('Enter a deadline for a new task: ')

        new_task = Task(name, short_desc, detailed_desc, deadline)
        new_task.id = self.db_worker.create_new_task(new_task)
        self.tasks.append(new_task)

    def change_status(self):
        pass

    def edit_task(self):
        pass
