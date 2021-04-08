from ORM import DataWork
from models_db import Task
# from utils import exit_program
from help_text import user_instruction
import sys
from settings import VALID_STATUSES, DB_NAME


def main():
    work = DataWork(DB_NAME)
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
                work.all_active_tasks()
            except:
                print("error happened in 'all_active_tasks' ")
            finally:
                continue
        elif action == 'completed':
            print(f'You selected the {action} command ')
            try:
                work.show_completed_tasks()
            except:
                print("error happened in 'show_completed_tasks' ")
        elif action == 'set status':
            while True:
                try:
                    task_id = input(f'You selected the {action} command, please enter a task id:  ')
                    new_status = input(f'Please, enter a new status for the task id - {task_id}: '
                                       f'(valid statuses are: New, In Progress, Closed): ')
                    if new_status in VALID_STATUSES:
                        # print(new_status)
                        # print(settings.VALID_STATUSES)
                        work.set_status(task_id, new_status)
                    else:
                        print('You are trying to set a wrong status for a task')
                    print(f'The new status "{new_status}" were set for the task with an id - "{task_id}"')
                    break
                except Exception as e:
                    print('error happened for "set_status"', e)
                    task_id = input(f'You selected the {action} command, please enter a task id:  ')
                    new_status = input(f'Please, enter a new status for the {task_id} '
                                       f'(valid statuses are: New, In Progress, Closed): ')
        elif action == 'show info':
            while True:
                try:
                    task_id = input(f'You selected the {action} command, please, enter the task id:  ')
                    work.show_info(task_id)
                    break
                except Exception as e:
                    print('You entered a wrong id number, there is an error happened', e)
                    task_id = input('Please enter an existing id of the task: ')
        elif action == 'exit':
            print(f'You selected the {action} command. Thank you. Bye!')
            break
        else:
            print('some error happened during interaction with a user')


if __name__ == '__main__':
    main()
