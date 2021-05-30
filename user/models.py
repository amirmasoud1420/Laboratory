from core.models import *


class User(BaseUser):
    id: int
    first_name: str
    last_name: str
    national_code: str
