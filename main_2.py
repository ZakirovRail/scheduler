from utils import authorisation, admin_or_user, exit_program
from db_main import DataWork
from help_text import user_instruction


def main():
    while True:
        action = input(f'{user_instruction}')
        if action == 'create':
            DataWork.create_new_task()
        if action == 'show':
            DataWork.show_all_user()
        if action == 'active':
            DataWork.all_active_for_user()
        if action == 'completed':
            DataWork.show_completed_user()
        if action == 'set <status> <id_task>':
            DataWork.set_status_user()
        if action == 'show info <id_task>':
            DataWork.show_info(id_task)
        if action == 'exit':
            exit_program()
        else:
            print('some error happened')
    else:
        pass  # there is should be redirect to authorisation


if __name__ == '__main__':
    main()
