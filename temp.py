# string = '/static/css/bootstrap.min.css'
# print(string[1:])


# string = 'email=login&password=123'
# data_list = string.split('&')
# data_dict = {}
# for item in data_list:
#     temp = item.split('=')
#     print(temp)
#     data_dict[temp[0]] = temp[1]
from models_db import UsersSession

token = '48548725a9bfbe25dd6ed6914f2e6f9a7b8ff7d6db9f809369271f3da69f6511'
result = UsersSession.get_by_token(token)
print(result)
