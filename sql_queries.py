create_task_table_command = """CREATE TABLE IF NOT EXISTS tasks (
	id integer PRIMARY KEY AUTOINCREMENT,
	title text NOT NULL,
    short_desc text NOT NULL,
    detailed_desc text NOT NULL,
    assigned_to text,
    date_creation datetime NOT NULL, 
	deadline datetime,
	status integer
);"""

create_users_table_command = """
        CREATE TABLE IF NOT EXISTS users (
	id integer PRIMARY KEY AUTOINCREMENT,
	user_name text NOT NULL,
	user_surname text NOT NULL,
	password text NOT NULL,
	reg_date text
);
"""

creat_admin_account_command = """
    INSERT INTO users(user_name, user_surname, password, reg_date)
    VALUES ('Mainaccount', 'Mainaccount', 'Mainpassword', datetime('now'));
"""


creat_new_task_command = """
        INSERT INTO tasks (title, short_desc, detailed_desc, assigned_to, date_creation, deadline, status)
    VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s');
"""

COLLUMNS = ['id', 'title', 'short_desc', 'detailed_desc', 'assigned_to', 'date_creation', 'deadline', 'status']

show_all_users_tasks = """
    SELECT * FROM tasks;
"""

show_all_active_tasks = """
    SELECT * FROM tasks where status in ('New', 'In Progress');
"""

show_completed_tasks_command = """
    SELECT * FROM tasks where status in ('Closed');
"""

delete_all_tasks_command = """
    DELETE FROM tasks;
"""

data_seeding_task_command_1 = """
    INSERT INTO tasks (title, short_desc, detailed_desc, assigned_to, date_creation, deadline, status)
    VALUES ('Default Task', 'A default task for testing DB', 'Some detailed description for a detailed task', 
    'User', datetime('now'), '31.12.2021', 'New');
"""
data_seeding_task_command_2 = """
    INSERT INTO tasks (title, short_desc, detailed_desc, assigned_to, date_creation, deadline, status)
    VALUES ('Default Task_2', 'A default task for testing DB_2', 'Some detailed description for a detailed task_2', 
    'User', datetime('now'), '25.12.2021', 'In Progress');
"""

data_seeding_task_command_3 = """
    INSERT INTO tasks (title, short_desc, detailed_desc, assigned_to, date_creation, deadline, status)
    VALUES ('Default Task_2', 'A default task for testing DB_2', 'Some detailed description for a detailed task_2', 
    'User', datetime('now'), '01.12.2021', 'Closed');
"""