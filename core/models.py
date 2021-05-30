from abc import ABC


class BaseModel(ABC):
    pass


class BaseUser(BaseModel, ABC):
    pass


class BaseMenu(BaseModel, ABC):
    pass
