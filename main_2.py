from ORM import DataWork
from models_db import Task, User
from utils import exit_program, encode_password
from help_text import user_instruction
import sys
from settings import VALID_STATUSES, DB_NAME
import logging
import actions

logger = logging.getLogger('scheduler')


def main():
    work = DataWork(DB_NAME)
    list_tasks = work.show_all_tasks(False)
    logger.debug(f'The following list_tasks - {list_tasks}')
    login_list = []
    current_user = actions.authorisation()

    while True:
        print(user_instruction)
        action = input('Your command: ')
        if action == 'create':
            print(f'You selected the {action} command ')
            try:
                new_task = Task()
                new_task.request_task_data()
                work.create_new_task(new_task)
                logger.debug(f'A new task were created: {new_task}')
            except Exception as e:
                logger.critical('Print error happened during creating a new task', e)
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
                logger.debug(f'The command to display a list of active tasks invoked')
            except Exception as e:
                logger.error(f'error happened in all_active_tasks - {repr(e)}')
            finally:
                continue
        elif action == 'completed':
            print(f'You selected the {action} command ')
            try:
                work.show_completed_tasks()
                logger.debug(f'The command to display a list of completed tasks invoked')
            except Exception as e:
                print("error happened in 'show_completed_tasks' ")
                logger.error(f'error happened in show_completed_tasks - {repr(e)}')
        elif action == 'set status':
            while True:
                try:
                    task_id = input(f'You selected the {action} command, please enter a task id:  ')
                    if int(task_id) in [int(item[0]) for item in list_tasks]:
                        new_status = input(f'Please, enter a new status for the task id - {task_id}: '
                                           f'(valid statuses are: New, In Progress, Closed): ')
                        logger.debug(f'A new status - {new_status} were selected for a task with id - {task_id}')
                        if new_status in list(Task.available_statuses.values()):
                            work.set_status(task_id, new_status)
                            logger.debug(f'A new status - {new_status} were set for a task with id - {task_id}')
                        else:
                            print('You are trying to set a wrong status for a task. Please try again.')
                            logger.debug(f'User tried to enter not existing status - {new_status}, the list of'
                                         f'available tasks statuses is - {list(Task.available_statuses.values())}')
                        break
                    else:
                        logger.error(f'User entered an not existing task id - {task_id}')
                except Exception as e:
                    print('error happened for "set_status"', e)
                    task_id = input(f'You selected the {action} command, please enter a task id:  ')
                    new_status = input(f'Please, enter a new status for the {task_id} '
                                       f'(valid statuses are: New, In Progress, Closed): ')
                    logger.error(f'error happened for "set_status"')
        elif action == 'show info':
            while True:
                task_id = input(f'You selected the {action} command, please, enter the task id:  ')
                try:
                    work.show_info(int(task_id))
                    logger.debug(f'The command to show info about a task were invoked')
                    break
                except Exception as e:
                    logger.critical('You entered a wrong id number, there is an error happened', e)
        elif action == 'edit':
            new_data = []
            while True:
                try:
                    task_id = input(f'You selected the {action} command, please, enter the task id or enter the "stop" command to stop:  ')
                    if task_id == 'stop':
                        print('You selected to stop, you will be return to a main menu')
                        break
                    if int(task_id) in [int(item[0]) for item in list_tasks]:
                        print(f'You entered the task id  = {task_id}')
                    else:
                        print('You entered a wrong task number, session will be closed. ')
                        break
                except Exception as e:
                    print('error happened for getting a task id', e)
                try:
                    new_short_desc = input(
                        'Enter a new short description, enter the "stop" to break or just hit the "Enter" key: ')
                    if new_short_desc == 'stop':
                        break
                    elif len(new_short_desc) == 0:
                        continue
                    else:
                        new_data.append(new_short_desc)
                except Exception as e:
                    print('error happened for getting a new short description', e)
                try:
                    new_detailed_desc = input(
                        'Enter a new detailed description, enter the "stop" to break or just hit the "Enter" key:')
                    if new_detailed_desc == 'stop':
                        logger.debug(f'User selected to stop interaction')
                        break
                    elif len(new_detailed_desc) == 0:
                        logger.debug(f'An empty new description')
                        continue
                    else:
                        new_data.append(new_detailed_desc)
                        logger.debug(f'The task with id = {task_id} were changed. New data is - {new_data}')
                except Exception as e:
                    logger.critical('error happened for getting a new detailed description', e)
                try:
                    # после обновления задачи снова цикл для обновления данных по задаче
                    #  не делал для изменения Title на случай если не правильно начал делать логику по обновлению данных
                    work.edit_task(task_id, new_data)
                    print('the new data is: ', new_data)
                    print(f'The task with id - {task_id} were updated')
                except Exception as e:
                    logger.critical('error happened for editing a task', e)
        elif action == 'delete':
            while True:
                try:
                    task_id = input(f'You selected the {action} command, please enter a task id:  ')
                    if int(task_id) in [int(item[0]) for item in list_tasks]:
                        work.delete_task(task_id)
                        logger.debug(f'A task with id = {task_id} were deleted')
                    else:
                        logger.error(f'A user is trying ti enter a not existing task id = {task_id}')
                    break
                except Exception as e:
                    logger.critical('error happened for "delete"', e)
        elif action == 'logout':
            print('You will be logout')
            current_user = actions.authorisation()
        elif action == 'exit':
            print(f'You selected the {action} command. Thank you. Bye!')
            logger.debug(f'The command to exit were invoked')
            break
        else:
            logger.error(f'some error happened during interaction with a user, probably user entered a wrong command.'
                         f'He entered the - "{action}" command')


if __name__ == '__main__':
    main()
