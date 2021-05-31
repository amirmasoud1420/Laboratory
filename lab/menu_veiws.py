from menu.models import *
from user.models import *
from datetime import date
from lab.models import *
import dill
import os


def corona_test_register():
    print("*Enter your information >")
    f_name = input("first_name : ")
    l_name = input("last_name : ")
    n_code = input("national_code : ")
    phone = input("phone_number : ")
    blood = input("blood group : ")
    p = Patient(f_name, l_name, n_code, phone, blood)

    print("you successfully registered...")
    d_date = date(year=date.today().year, month=date.today().month, day=date.today().day)
    r_date = date(year=date.today().year, month=date.today().month, day=date.today().day)
    print("please come to labratoary for ddoing test in : ", d_date)
    print("your result is ready in : ", r_date)
    c_test = CoronaTest(p, d_date, r_date)
    with open(f"files\corona_tests\{p.national_code}.txt", 'wb') as f:
        dill.dump(p, f)
    with open(f"files\corona_tests\{p.national_code}.txt", 'wb') as f:
        dill.dump(c_test, f)


def corona_test_view_result():
    n_code = input("pleas enter your national code : ")
    if os.path.exists(f"files\corona_tests\{n_code}.txt"):
        with open(f"files\corona_tests\{n_code}.txt", 'rb') as f:
            c_test = dill.load(f)
        print('your result is : ', c_test.rsult)
    else:
        print("your national code is not exist!!!")


# register_corona_test_menu_view = MenuView(corona_test_register())
# view_result_corona_test_menu_view = MenuView(corona_test_view_result())
