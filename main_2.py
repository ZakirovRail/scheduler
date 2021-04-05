from db_main_com import DataWork
from utils import authorisation, admin_or_user, exit_program
from help_text import user_instruction
import sys


def main():

    while True:
        print(user_instruction)
        action = input('Your command: ')
        if action == 'create':
            print(f'You selected the {action} command ')
            try:
                DataWork.create_new_task()
            except:
                print("error happened")
            finally:
                continue
        if action == 'show':
            print(f'You selected the {action} command ')
            try:
                DataWork.show_all_tasks()
            except:
                print("error happened")
            finally:
                continue
        if action == 'active':
            print(f'You selected the {action} command ')
            try:
                DataWork.all_active_tasks()
            except:
                print("error happened")
            finally:
                continue
        if action == 'completed':
            print(f'You selected the {action} command ')
            try:
                DataWork.show_completed_user()
            except:
                print("error happened")
            finally:
                continue
        if action == 'set <status> <id_task>':
            print(f'You selected the {action} command ')
            try:
                DataWork.set_status_user()
            except:
                print("error happened")
            finally:
                continue
        if action == 'show info <id_task>':
            print(f'You selected the {action} command ')
            try:
                DataWork.show_info(id_task)
            except:
                print("error happened")
            finally:
                continue
        if action == 'exit':
            try:
                exit_program()
            except:
                print("error happened")
            finally:
                sys.exit(0)
        else:
            print('some error happened')


if __name__ == '__main__':
    main()
