from lab.models import *
from user.models import *
from datetime import date, datetime, timedelta


def register_test(test: Test):
    f_name = input("input your first name : ")
    l_name = input("input your last name : ")
    phone = input("input your phone number : ")
    n_code = input("input your national code : ")
    birth_date = input("input your birth_date : ")

    p = Patient(f_name, l_name, n_code, phone, birth_date)  # should be create in data base

    doing_date = date.today()
    result_date = doing_date + timedelta(days=test.duration)
    doctor = Doctor('akbar', 'asqar', 1234, 1234)  # should be read from data base

    test_list = TestList(test, p, doctor, doing_date, result_date)  # should be create in data base

    print("register done...")

def add_test():
    pass

