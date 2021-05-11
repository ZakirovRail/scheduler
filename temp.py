# string = '/static/css/bootstrap.min.css'
# print(string[1:])


string = 'email=login&password=123'
data_list = string.split('&')
data_dict = {}
for item in data_list:
    temp = item.split('=')
    print(temp)
    data_dict[temp[0]] = temp[1]



