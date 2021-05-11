from actions import *

urls_dict = [
    {'pattern': '/main/', 'method': main_page, },
    {'pattern': '/login/', 'method': users.login, },
    {'pattern': '/registration/', 'method': users.register, },
    {'pattern': '/create/', 'method': tasks.create_task_action, },
    {'pattern': '/show/', 'method': tasks.show_action, },
    {'pattern': '/active/', 'method': tasks.active_action, },
    {'pattern': '/completed/', 'method': tasks.completed_action, },
    {'pattern': '/set_status/<id>/', 'method': tasks.set_status_action, },
    {'pattern': '/show_info/<id>/', 'method': tasks.show_info_action, },
    {'pattern': '/edit/<id>/', 'method': tasks.edit_action, },
    {'pattern': '/delete/<id>/', 'method': tasks.delete_action, },
    # {'pattern': 'logout/', 'method': , },
]

path_example = 'main/'


def get_function(path):
    list_par = path.split('/')
    weight = 0
    name = None
    pattern = None
    params = []
    for url in urls_dict:
        weight_tmp = 0
        list_patterns_path = url['pattern'].split('/')
        if len(list_par) == len(list_patterns_path):
            for i in range(len(list_patterns_path)):
                if list_patterns_path[i] == list_par[i]:
                    weight_tmp += 1
        if weight_tmp > weight:
            weight = weight_tmp
            name = url['method']
            pattern = url['pattern']
    try:
        pattern_split = pattern.split('/')
        for i in range(len(pattern_split)):
            if pattern_split[i] != list_par[i]:
                params.append(list_par[i])
    except Exception as e:
        print('Here an exception', e)
    return name, params


if __name__ == '__main__':
    get_function(path_example)
