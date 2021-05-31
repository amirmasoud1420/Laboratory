from core.models import *
from user.models import *
from datetime import date


class Test(BaseModel):
    pass


class CoronaTest(Test):
    def __init__(self,patient: Patient,do_date,result_date,result= None):
        self.result = result
        self.patient = patient
        self.do_date = do_date
        self.result_date = result_date
