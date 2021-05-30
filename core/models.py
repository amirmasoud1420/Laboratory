from abc import ABC


class BaseModel(ABC):
    id: int
    pass


class BaseUser(BaseModel):
    pass


class BaseMenu(BaseModel):
    pass
