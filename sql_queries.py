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

select_all_from_users_table = """
    SELECT * FROM users;
"""


creat_new_task_command = """
        INSERT INTO tasks (title, short_desc, detailed_desc, assigned_to, date_creation, deadline, status)
    VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s');
"""

show_all_users_tasks = """
    SELECT * FROM tasks;
"""