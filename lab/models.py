from core.models import *
from user.models import *
from datetime import date


class Test(BaseModel):
    id: int

    def __init__(self, name, price, duration=5, description=""):
        self.name = name
        self.price = price
        self.duration = duration
        self.description = description


# corona_test = Test('corona', 1000, 4, 'corona test')


class TestList:
    id: int

    def __init__(self, test: Test, patient: Patient, doctor: Doctor, doing_date: date, result_date: date,
                 result: str = "Not Ready"):
        self.test = test
        self.patient = patient
        self.doctor = doctor
        self.doing_date = doing_date
        self.result_date = result_date
        self.result = result
