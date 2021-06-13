from core.models import *


class User(BaseUser):
    id: int
    first_name: str
    last_name: str
    national_code: str
    phone_number: str


class Patient(User):
    def __init__(self, f_name, l_name, n_code, phone_number, birth_date):
        self.first_name = f_name
        self.last_name = l_name
        self.national_code = n_code
        self.phone_number = phone_number
        self.birth_date = birth_date


class Doctor(User):
    def __init__(self, f_name, l_name, p_code, password):
        self.first_name = f_name
        self.last_name = l_name
        self.personal_code = p_code
        self.password = password


class Admin(User):
    def __init__(self, username, password):
        self.username:str = username
        self.password:str = password
