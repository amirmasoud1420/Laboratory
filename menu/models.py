from core.models import *


class Node(BaseMenu):

    def __init__(self, parent=None):
        self.parent = parent
        self.children = []
        if self.parent:
            self.parent.children.append(self)


class Menu(Node):
    def __init__(self, name, parent=None):
        Node.__init__(self, parent)
        self.name = name

    def __call__(self, *args, **kwargs):
        pass

    def __repr__(self):
        return f"{self.name}"


class MenuList(Menu):
    def __call__(self, *args, **kwargs):
        print(self, " : ")
        print('>>>>')
        print("0 : Exit")
        if self.children:
            for n, i in enumerate(self.children):
                print(n + 1, ":", i)
        n = int(input("Enter your choice : "))
        if n == 0:
            if self.parent:
                self.parent()
            else:
                exit()
        else:
            self.children[n - 1]()


class MenuView(Menu):
    def __init__(self, function, name=None, parent=None, *args, **kwargs):
        if not name:
            name = function.__name__
        super().__init__(name, parent)
        self.function = function
        self.args = args
        self.kwargs = kwargs

    def __call__(self, *args, **kwargs):
        self.function(*self.args, **self.kwargs)
        if self.parent:
            self.parent()
        else:
            exit()
