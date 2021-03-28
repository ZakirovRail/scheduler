from utils import authorisation, admin_or_user, exit_program
from db_main import DataWork

admin_instruction = """
1. To creat a new task enter 'create': 
2. To display all existing tasks enter 'show': 
3. To display only active tasks enter 'active': 
4. To display only completed tasks enter 'completed': 
5. To delete all tasks enter 'delete all': 
6. To delete a tasks enter 'delete <id_task>': 
7. To show all users enter 'show users': 
8. To change assignment for a task enter  'assign <id_task> <id_user>': 
9. To set up a status (New, In_Progress, Done) for a task enter 'set <status> <id_task>':
10. To show an information about a task, enter 'show info <id_task>'
11. To exit, enter 'exit': 
"""

user_instruction = """
1. To creat a new task enter 'create': 
2. To display all existing tasks enter 'show': 
3. To display only active tasks enter 'active': 
4. To display only completed tasks enter 'completed': 
5. To set up a status (New, In_Progress, Done) for a task enter 'set <status> <id_task>': 
6. To show an information about a task, enter 'show info <id_task>'
7. To exit, enter 'exit':
"""


def main():
    while True:
        if authorisation:
            if 'admin' in admin_or_user:
                action = input(f'{admin_instruction}')
                if action == 'create':
                    DataWork.create_new_task()
                if action == 'show':
                    DataWork.show_all_tasks_admin()
                if action == 'active':
                    DataWork.all_active_for_admin()
                if action == 'completed':
                    DataWork.show_completed_for_all()
                if action == 'delete all':
                    DataWork.delete_all_tasks()
                if action == 'delete <id_task>':
                    DataWork.delete_task()
                if action == 'show users':
                    DataWork.show_all_user()
                if action == 'assign <id_task> <id_user>':
                    DataWork.assign_task()
                if action == 'set <status> <id_task>':
                    DataWork.set_status_admin()
                if action == 'show info <id_task>':
                    DataWork.show_info(id_task)
                if action == 'exit':
                    exit_program()
                # not clear what next?
            elif 'user' in admin_or_user:
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
                print('some error happens during determining a user role')
        else:
            pass  # there is should be redirect to authorisation


if __name__ == '__main__':
    main()
