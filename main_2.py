from tabulate import tabulate

from ORM import DataWork
from models_db import Task
from sql_queries import COLLUMNS
from utils import exit_program
from help_text import user_instruction
import sys
import settings


def main():
    work = DataWork(settings.DB_NAME)
    while True:
        print(user_instruction)
        action = input('Your command: ')
        if action == 'create':
            print(f'You selected the {action} command ')
            try:
                new_task = Task()
                new_task.request_task_data()
                work.create_new_task(new_task)
            except:
                print("error happened during creating a new task")
        elif action == 'show':
            print(f'You selected the {action} command ')
            try:
                list_tasks = work.show_all_tasks()
                Task.print_tasks(list_tasks)
            except:
                print("error happened")
        elif action == 'active':
            print(f'You selected the {action} command ')
            try:
                DataWork.all_active_tasks()
            except:
                print("error happened")
            finally:
                continue
        elif action == 'completed':
            print(f'You selected the {action} command ')
            try:
                DataWork.show_completed_user()
            except:
                print("error happened")
            finally:
                continue
        elif action == 'set <status> <id_task>':
            print(f'You selected the {action} command ')
            try:
                DataWork.set_status_user()
            except:
                print("error happened")
            finally:
                continue
        elif action == 'show info <id_task>':
            print(f'You selected the {action} command ')
            try:
                DataWork.show_info(id_task)
            except:
                print("error happened")
            finally:
                continue
        elif action == 'exit':
            try:
                exit_program()
            except:
                print("error happened")
            finally:
                sys.exit(0)
        else:
            print('some error happened during interaction with a user')


if __name__ == '__main__':
    main()
