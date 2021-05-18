from actions.users import *
from actions.tasks import *
from utils import render_template


def main_page(request):
    return render_template('templates/index.html')
