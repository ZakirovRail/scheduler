from ORM import DataWork
from actions.tasks import create_task_action, show_action, active_action, completed_action, set_status_action, \
    show_info_action, edit_action, delete_action
from actions.users import authorisation
from help_text import user_instruction
from settings import DB_NAME
import logging

logger = logging.getLogger('scheduler')


def main():
    work = DataWork(DB_NAME)
    list_tasks = work.show_all_tasks(False)
    logger.debug(f'The following list_tasks - {list_tasks}')
    login_list = []
    current_user = authorisation()

    while True:
        print(user_instruction)
        action = input('Your command: ')
        if action == 'create':
            print(f'You selected the {action} command ')
            create_task_action()
        elif action == 'show':
            print(f'You selected the {action} command ')
            logger.debug(f'The "show" command were selected')
            show_action()
        elif action == 'active':
            print(f'You selected the {action} command ')
            active_action()
            # ??? Как поступить с циклом While еслив ынести в функцию active_action()???
            # try:
            #     work.all_active_tasks()
            #     logger.debug(f'The command to display a list of active tasks invoked')
            # except Exception as e:
            #     logger.error(f'error happened in all_active_tasks - {repr(e)}')
            # finally:
            #     continue
        elif action == 'completed':
            print(f'You selected the {action} command ')
            completed_action()
        elif action == 'set status':
            set_status_action(action)
        elif action == 'show info':
            show_info_action(action)
        elif action == 'edit':
            edit_action(action)
        elif action == 'delete':
            delete_action(action)
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
