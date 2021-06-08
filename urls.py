from actions import *
import logging

logger = logging.getLogger('scheduler')

urls_dict = [
    {'pattern': '/', 'method': main_page, },
    # {'pattern': '/main/', 'method': main_page, },
    {'pattern': '/login/', 'method': users.login, },
    {'pattern': '/registration/', 'method': users.register, },
    {'pattern': '/create/', 'method': tasks.create_task_action, },
    {'pattern': '/show/', 'method': tasks.show_action, },
    {'pattern': '/active/', 'method': tasks.active_action, },
    {'pattern': '/completed/', 'method': tasks.completed_action, },
    {'pattern': '/set_status/<id>/', 'method': tasks.set_status_action, },
    {'pattern': '/close/<task_id>/', 'method': tasks.close_task, },
    {'pattern': '/show_info/<id>/', 'method': tasks.show_info_action, },
    {'pattern': '/edit/<id>/', 'method': tasks.edit_action, },
    {'pattern': '/delete/<id>/', 'method': tasks.delete_action, },
    # {'pattern': 'logout/', 'method': , },
]

path_example = 'main/'


def get_function(path):
    list_par = path.split('/')  # make here a trim
    weight = 0
    name = None
    pattern = None
    params = []
    for url in urls_dict:
        weight_tmp = 0
        list_patterns_path = url['pattern'].split('/')   # make here a trim
        logger.debug(f'The list_patterns_path is: {list_patterns_path}')
        if len(list_par) == len(list_patterns_path):
            for i in range(len(list_patterns_path)):
                if list_patterns_path[i] == list_par[i]:
                    weight_tmp += 1
        if weight_tmp > weight and weight_tmp > 2 and len(list_par) > 2:
            weight = weight_tmp
            name = url['method']
            pattern = url['pattern']
        elif len(list_par) <= 2 and weight_tmp > weight:
            weight = weight_tmp
            name = url['method']
            pattern = url['pattern']
    try:
        if pattern is not None:
            pattern_split = pattern.split('/')
            for i in range(len(pattern_split)):
                if pattern_split[i] != list_par[i]:
                    params.append(list_par[i])
            logger.debug(f'Params list is: {params}')
        # in ELSE block will be empty parameters
    except Exception as e:
        logger.critical(f'An exception while splitting the path {path}: ', e)
    return name, params


if __name__ == '__main__':
    get_function(path_example)
