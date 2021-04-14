from models_db import Task
from ORM import DataWork

# print(dir(Task.available_statuses.values()))
# print(list(Task.available_statuses.values()))

ex = DataWork('scheduler.db')
list_tasks = ex.show_all_tasks()
# print(dir(list_tasks))

# for item in list_tasks:
#     print(item)
#     print('The id is - ', item[0])
list_gen = [item[0] for item in list_tasks]
print(list_gen)
