from actions import *
from help_text import user_instruction
import logging

logger = logging.getLogger('scheduler')


def main():
    # work = DataWork(DB_NAME)
    # list_tasks = work.show_all_tasks(False)
    # logger.debug(f'The following list_tasks - {list_tasks}')
    # login_list = []
    current_user = authorisation()

    while True:
        print(user_instruction)
        action = input('Your command: ')
        if action == 'create':
            print(f'You selected the {action} command ')
            create_task_action(current_user)
        elif action == 'show':
            print(f'You selected the {action} command ')
            logger.debug(f'The "show" command were selected')
            show_action(current_user)
        elif action == 'active':
            print(f'You selected the {action} command ')
            active_action(current_user)
        elif action == 'completed':
            print(f'You selected the {action} command ')
            completed_action(current_user)
        elif action == 'set status':
            set_status_action(action, current_user)
        elif action == 'show info':
            show_info_action(action, current_user)
        elif action == 'edit':
            edit_action(action, current_user)
        elif action == 'delete':
            delete_action(action, current_user)
        elif action == 'logout':
            print('You will be logout')
            current_user = authorisation()
        elif action == 'exit':
            print(f'You selected the {action} command. Thank you. Bye!')
            logger.debug(f'The command to exit were invoked')
            break
        else:
            logger.error(f'some error happened during interaction with a user, probably user entered a wrong command.'
                         f'He entered the - "{action}" command')


if __name__ == '__main__':
    main()
