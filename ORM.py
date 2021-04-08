from tabulate import tabulate

from db_main_com import BaseDB
from sql_queries import COLLUMNS, delete_all_tasks_command, show_completed_tasks_command, show_all_active_tasks, \
    show_all_users_tasks, creat_new_task_command


class DataWork(BaseDB):

    def __init__(self, db_file):
        super().__init__(db_file)

    def show_info(self, id_task):
    #     """
    #     get an information about current tasks for a logged user
    #     :return:
    #     """
    #     id_task = id_task
        pass

    def create_new_task(self, task):
        """
        To add a new task for a current account
        :return:
        """
        local_id = None
        try:
            c = self.conn.cursor()
            c.execute(creat_new_task_command, [task.title, task.short_desc, task.detailed_desc, task.assigned_to,
                                               task.date_creation, task.deadline, task.status])
            local_id = c.fetchone()[0]
            self.conn.commit()
            print(creat_new_task_command)
        except Exception as e:
            print('print from create_new_task', e)
        return local_id

    def show_all_tasks(self):
        """
        the method which will return all existing tasks. For admin account only
        :return:
        """
        list_tasks = []
        try:
            c = self.conn.cursor()
            c.execute(show_all_users_tasks)
            list_tasks = c.fetchall()
        except Exception as e:
            print('print from show_all_tasks', e)
        return list_tasks

    def all_active_tasks(self):
        list_active_tasks = []
        try:
            c = self.conn.cursor()
            c.execute(show_all_active_tasks)
            list_active_tasks = c.fetchall()
        except Exception as e:
            print('print from all_active_tasks', e)
        return print(tabulate(list_active_tasks, headers=COLLUMNS), '\n')

    def show_completed_tasks(self):
        list_completed_tasks = []
        try:
            c = self.conn.cursor()
            c.execute(show_completed_tasks_command)
            list_completed_tasks = c.fetchall()
        except Exception as e:
            print('print from show_completed_tasks', e)
        return print(tabulate(list_completed_tasks, headers=COLLUMNS), '\n')

    def set_status(self, id_task):
        pass

    def delete_all_tasks(self):
        try:
            c = self.conn.cursor()
            c.execute(delete_all_tasks_command)
            self.conn.commit()
        except Exception as e:
            print('print from delete_all_tasks', e)
        return print('Deleted all tasks from DB')

    def delete_task(self, id_task):
        pass


if __name__ == '__main__':
    pass
