from core.app import *
from lab.manager import *


def home():
    tm = test_Manager()
    test_list = tm.read_all()
    return render_template('home.html',tests=test_list)

