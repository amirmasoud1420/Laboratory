from core.models import *


class User(BaseUser):
    id: int
    first_name: str
    last_name: str
    national_code: str
    phone_number: str


class Patient(User):
    def __init__(self, f_name, l_name, n_code, phone_number, blood):
        self.first_name = f_name
        self.last_name = l_name
        self.national_code = n_code
        self.phone_number = phone_number
        self.blood_group = blood
