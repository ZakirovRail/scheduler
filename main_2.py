from ORM import DataWork
from models_db import Task
# from utils import exit_program
from help_text import user_instruction
import sys
from settings import VALID_STATUSES, DB_NAME
import logging

logger = logging.getLogger('scheduler')


def main():
    work = DataWork(DB_NAME)
    list_tasks = work.show_all_tasks(False)
    logger.debug(f'The following list_tasks - {list_tasks}')
    login_list = []
    current_user = None

    while True:
        login = str(input('Enter your login'))
        if login in login_list:
            for _ in range(3):
                password = (input('Enter your password'))
                if hash.password == hash.stored_password(login):
                    current_user = get_user(login)
                    break
                else:
                    print('You entered a wrong password. Try again')
        if current_user is None:
            print('User is not defined, the session will be closed')
            sys.exit(1)

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
            logger.debug(f'The "show" command were selected')
            try:
                list_tasks = work.show_all_tasks()
                # Task.print_tasks(list_tasks)
                logger.debug(f'The "show" command were selected')
            except Exception as e:
                logger.error(f'Error happened during showing all records - {str(e)}')
                logger.error(f'Error happened during showing all records - {repr(e)}')
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
                    if int(task_id) in [int(item[0]) for item in list_tasks]:
                        new_status = input(f'Please, enter a new status for the task id - {task_id}: '
                                           f'(valid statuses are: New, In Progress, Closed): ')
                        if new_status in list(Task.available_statuses.values()):
                            work.set_status(task_id, new_status)
                            print(f'The new status "{new_status}" were set for the task with an id - "{task_id}"')
                        else:
                            print('You are trying to set a wrong status for a task. Please try again.')
                        break
                    else:
                        print('You are entered an not existing task id')
                except Exception as e:
                    print('error happened for "set_status"', e)
                    task_id = input(f'You selected the {action} command, please enter a task id:  ')
                    new_status = input(f'Please, enter a new status for the {task_id} '
                                       f'(valid statuses are: New, In Progress, Closed): ')
        elif action == 'show info':
            while True:
                task_id = input(f'You selected the {action} command, please, enter the task id:  ')
                try:
                    work.show_info(int(task_id))
                    break
                except Exception as e:
                    print('You entered a wrong id number, there is an error happened', e)
        elif action == 'exit':
            print(f'You selected the {action} command. Thank you. Bye!')
            break
        else:
            print('some error happened during interaction with a user')


if __name__ == '__main__':
    main()
