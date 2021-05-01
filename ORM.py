
from tabulate import tabulate

from db_main_com import BaseDB
from sql_queries import COLLUMNS, delete_all_tasks_command, show_completed_tasks_command, \
    show_all_active_tasks_command, show_all_users_tasks_command, creat_new_task_command, show_task_info_command

import logging

logger = logging.getLogger('scheduler')


class DataWork(BaseDB):

    def __init__(self, db_file):
        super().__init__(db_file)

    def show_info(self, task_id, user_id: str,):
        task_id = task_id
        task_info = []
        try:
            c = self.conn.cursor()
            c.execute("SELECT * FROM tasks where id=(?) and assigned_to=(?)", (task_id, user_id, ))
            task_info = c.fetchall()
            logger.debug(f'The task_info is following: {task_info}')
        except Exception as e:
            logger.critical('Error from show_info: ', e)
        return print(tabulate(task_info, headers=COLLUMNS), '\n')

    def create_new_task(self, task):
        """
        To add a new task for a current account
        :return:
        """
        local_id = None
        try:
            c = self.conn.cursor()
            new_task_tuple = (task.title, task.short_desc, task.detailed_desc, task.assigned_to, task.date_creation,
                              task.deadline, task.status, )

            c.execute(creat_new_task_command, new_task_tuple)
            print("SQL - ", c.fetchone())
            # local_id = c.fetchone()[0]  # None is returned
            self.conn.commit()
            logger.debug(f'The new task method was invoked. The info about the task: {task}')
        except Exception as e:
            logger.critical('Error print from create_new_task method: ', e)
        return local_id

    def show_all_tasks(self, user_id: str, need_print=True):
        """
        the method which will return all existing tasks. For admin account only
        :return:
        """
        list_tasks = []
        try:
            c = self.conn.cursor()
            c.execute(show_all_users_tasks_command, (user_id, ))
            list_tasks = c.fetchall()
            logger.debug(f'The list of tasks is the following: {list_tasks}')
        except Exception as e:
            logger.critical('print from show_all_tasks', e)
        if need_print:
            print(tabulate(list_tasks, headers=COLLUMNS), '\n')
        return list_tasks

    def all_active_tasks(self, user_id: str):
        list_active_tasks = []
        try:
            c = self.conn.cursor()
            c.execute(show_all_active_tasks_command, (user_id, ))
            list_active_tasks = c.fetchall()
            logger.debug(f'The list of active tasks is following: {list_active_tasks}')
        except Exception as e:
            logger.critical('Error print from all_active_tasks', e)
        return print(tabulate(list_active_tasks, headers=COLLUMNS), '\n')

    def show_completed_tasks(self, user_id: str):
        list_completed_tasks = []
        try:
            c = self.conn.cursor()
            c.execute(show_completed_tasks_command, (user_id, ))
            list_completed_tasks = c.fetchall()
            logger.debug(f'The completed tasks is following: {list_completed_tasks}')
        except Exception as e:
            logger.critical('Error print from show_completed_tasks', e)
        return print(tabulate(list_completed_tasks, headers=COLLUMNS), '\n')

    def set_status(self, task_id, new_status):
        task_id = task_id
        status = new_status
        try:
            c = self.conn.cursor()
            c.execute("UPDATE tasks SET status = (?) where id = (?);", (status, task_id, ))
            self.conn.commit()
            logger.debug(f'Will be set a status - {status} for a task with id- {task_id}')
        except Exception as e:
            logger.critical('Error print from set_status', e)

    def edit_task(self, task_id, new_data: list, user_id: str):
        task_id = task_id
        new_short_desc = new_data[0]
        new_detailed_desc = new_data[1]
        try:
            c = self.conn.cursor()
            c.execute("UPDATE tasks SET short_desc = (?), detailed_desc = (?) where id = (?) and assigned_to = (?);",
                      (new_short_desc, new_detailed_desc, task_id, user_id))
            self.conn.commit()
            logger.debug(f'The task is edited: task_id = {task_id}, new_short_desc = {new_short_desc},'
                         f'new_detailed_desc={new_detailed_desc}')
        except Exception as e:
            logger.critical('Error print from set_status', e)

    def delete_all_tasks(self, user_id: str):
        try:
            c = self.conn.cursor()
            c.execute(delete_all_tasks_command, (user_id, ))
            self.conn.commit()
            logger.debug(f'The delete all tasks command was invoked')
        except Exception as e:
            logger.critical('Error print from delete_all_tasks', e)
        return print('Deleted all tasks from DB')

    def delete_task(self, task_id, user_id: str):
        task_id = task_id
        try:
            c = self.conn.cursor()
            c.execute("DELETE from tasks where id = (?) and assigned_to = (?);", (task_id, user_id, ))
            self.conn.commit()
            logger.debug(f'The task with id were deleted: task_id = {task_id}')
        except Exception as e:
            logger.critical('Error print from delete_all_tasks', e)
        return print(f'Deleted tasks from DB with the id - "{task_id}"')


if __name__ == '__main__':
    pass
