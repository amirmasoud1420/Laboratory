from user.managers import *
from user.models import Admin
from lab.manager import *
from lab.models import *

# conn: connection = connect("dbname='labratoary' host='localhost' user='postgres' password='am14201378'")
#
# print(conn)
#
# curs: cursor = conn.cursor()
# a = Admin('admin', '1234')
# a=f"INSERT INTO admin(username,password) VALUES ('{a.username}','{a.password}')"
# print(a)
# curs.execute(a)
# conn.commit()
# conn.close()

m = Adimn_Manager()
# a = m.read('admin1', '1234')
# if not a:
#     print('not found')
# else:
#     print('u : ',a.username)
#     print('p : ',a.password)

# m.delete(Admin('my_admin', '12345'))
# m.creat(Admin('admin','1234'))
# m.update(Admin('my_admin', '1234'), Admin('my_admin', '12345'))

# md = Doctor_Manager()
d1 = Doctor('amir', 'talebi', '1234', '1234')
# md.creat(d1)
# d2 = md.read('1234','1234')
# if not d2:
#     print('not found')
# else:
#     print(d2.first_name,d2.last_name)

d2 = Doctor('amirmasoud', 'talebnia', '1234', '1234')
# md.update(d1,d2)
# md.delete(d2)


# mp = Patient_Manager()
p1 = Patient('amir', 'kiani', '1234', '09112223456', '2000-01-01')
# mp.creat(p1)
# p = mp.read('09112223456', '1234')
# if not p:
#     print('not found')
# else:
#     print(p.first_name, p.last_name)

p2 = Patient('hosein', 'ghanavati', '1234', '09112223456', '2000-01-01')
# mp.update(p1, p2)
# mp.delete(p2)
# mp.creat(p1)


tm = test_Manager()

t = Test('cvc',2000)
tm.creat(t)