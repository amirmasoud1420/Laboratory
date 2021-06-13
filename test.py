from menu.models import *
from lab.models import *
from user.menu_veiws import *

corona_test = Test('corona test', 1000)  # should be read from data base
cvc = Test('cvc', 200)  # should be read from data base
sugar = Test('sugar', 1000)  # should be read from data base
blood = Test('blood', 1000)  # should be read from data base
'''main menu'''
main_menu = MenuList('main_menu')

'''choose role menu'''
doctor_menu = MenuList('doctor', main_menu)
admin_menu = MenuList('admin', main_menu)
patient_menu = MenuList('patient', main_menu)

'''patient_menu'''
register_test_menu = MenuList('do a test', patient_menu)
view_test_menu = MenuView(register_test, 'view test', patient_menu, cvc)

corona_menu = MenuView(register_test, f'{corona_test.name}', register_test_menu, corona_test)
cvc_menu = MenuView(register_test, f'{cvc.name}', register_test_menu, cvc)
sugar_menu = MenuView(register_test, f'{sugar.name}', register_test_menu, sugar)
blood_menu = MenuView(register_test, f'{blood.name}', register_test_menu, blood)


'''admin menu'''
def login():
    input("enter your name")
    admin()


admin_login_menu = MenuView(login, 'login', admin_menu)
admin_register_menu = MenuView(register_test, 'register', admin_menu, cvc)
admin = MenuList('admin')
add_test_menu = MenuView(register_test, 'add a test', admin, cvc)
delete_test_menu = MenuView(register_test, 'delete a test', admin, cvc)
update_test_menu = MenuView(register_test, 'update a test', admin, cvc)

'''doctor menu'''

main_menu()
