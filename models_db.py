import datetime
from abc import ABC
from typing import List
from ORM import DataWork
from tabulate import tabulate

from sql_queries import COLLUMNS


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
                break
            except:
                task_deadline = input('Please enter a correct format of data, which is  - dd.mm.yyyy')
        self.date_creation = datetime.datetime.now()
        self.status = 1

    @staticmethod
    def print_tasks(list_tasks):
        # print(tabulate(list_tasks, headers=COLLUMNS))
        for task_item in list_tasks:
            task_item.print_one_tasks()

    def print_one_tasks(self, is_short_view=True):
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
            # print(f'id: {task["id"]}, title: {title}, short_desc:{short_desc},
            # detailed_desc:{detailed_desc}, assigned_to:{assigned_to},'
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


if __name__ == '__main__':
    pass
