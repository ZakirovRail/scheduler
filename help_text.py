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
Hello, please enter the appropriate command:
1. To creat a new task enter "create": 
2. To display all existing tasks enter "show": 
3. To display only active tasks enter "active": 
4. To display only completed tasks enter "completed": 
5. To set up a status (New, In_Progress, Done) for a task enter "set status": 
6. To show an information about a task, enter "show info":
7. To edit a task, enter 'edit':
8. To delete all tasks (for Admin only): select "delete all": 
9. To delete a specific task, select "delete": 
10. To logout, enter "logout":
11. To exit, enter "exit":
"""