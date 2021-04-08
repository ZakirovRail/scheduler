from ORM import DataWork
from sql_queries import create_task_table_command, create_users_table_command, creat_admin_account_command, \
    data_seeding_task_command_1, data_seeding_task_command_2, data_seeding_task_command_3
from db_main_com import BaseDB
import settings


class CreatDB(BaseDB):
    """
    This class for creating a new DB and creating a default admin account
    """
    def __init__(self, db_file):
        super().__init__(db_file)

    def create_tasks_table(self):
        """
        create a new tasks table in the DB SQLite for tasks
        :return:
        """
        try:
            c = self.conn.cursor()
            c.execute(create_task_table_command)
        except Exception as e:
            print('print from create_tasks_table', e)

    def creat_users_table(self):
        """
        create a new DB SQLite for users
        :return:
        """
        try:
            c = self.conn.cursor()
            c.execute(create_users_table_command)
        except Exception as e:
            print('print from creat_users_table', e)

    def create_admin_account(self):
        """
        create a default admin account during deploying a new DB
        :return:
        """
        try:
            c = self.conn.cursor()
            c.execute(creat_admin_account_command)
            print(creat_admin_account_command)
        except Exception as e:
            print('print from create_admin_account', e)


class DataSeeding(BaseDB):
    """
    This class for data seeding a new DB and creating a default tasks
    """
    def __init__(self, db_file):
        super().__init__(db_file)

    def data_seeding(self):
        """
        create a new DB SQLite for tasks
        :return:
        """
        try:
            c = self.conn.cursor()
            c.execute(data_seeding_task_command_1)
            c.execute(data_seeding_task_command_2)
            c.execute(data_seeding_task_command_3)
            self.conn.commit()
        except Exception as e:
            print('print from create_tasks_table', e)


if __name__ == '__main__':

    create_db = CreatDB(settings.DB_NAME)
    create_db.create_tasks_table()
    create_db.creat_users_table()

    seeding = DataSeeding(settings.DB_NAME)
    seeding.data_seeding()

    work_data = DataWork(settings.DB_NAME)
    work_data.show_all_tasks()
    work_data.all_active_tasks()
    work_data.show_completed_tasks()
    work_data.delete_all_tasks()
