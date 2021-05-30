from abc import ABC,abstractmethod


class BaseManager(ABC):
    @abstractmethod
    def creat(self):
        pass

    @abstractmethod
    def read(self):
        pass
    @abstractmethod
    def update(self):
        pass
    @abstractmethod
    def delete(self):
        pass