from menu.models import *

def test():
    print("salam asqar!!!")


first_menu = MenuList('root')
akbar = MenuList('akbar', parent=first_menu)
asqar = MenuView(test, 'asqar', parent=akbar)

first_menu()
