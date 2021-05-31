from menu.models import *
from lab.models import *
from lab.menu_veiws import *
def test():
    print("salam asqar!!!")

#
# first_menu = MenuList('root')
# akbar = MenuList('akbar', parent=first_menu)
# asqar = MenuView(test, 'asqar', parent=akbar)
#
# first_menu()

main_menu = MenuList('main_menu')
register_corona_test_menu_view = MenuView(corona_test_register,parent=main_menu)
view_result_corona_test_menu_view = MenuView(corona_test_view_result,parent=main_menu)

main_menu()