from core.manager import *
from psycopg2 import connect
from psycopg2._psycopg import connection, cursor
from lab.models import *


class test_Manager(DatabaseManager):
    def __init__(self):
        self.conn: connection = connect("dbname='labratoary' host='localhost' user='postgres' password='pass'")
        self.curs: cursor = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    def creat(self, t: Test):
        self.curs.execute(f"INSERT INTO test(name,price,description) VALUES ('{t.name}','{t.price}','{t.description}')")
        self.conn.commit()

    def read(self, name: str):
        try:
            self.curs.execute(f"SELECT * FROM test where uname='{name}'")
            lis = self.curs.fetchone()
            return Test(lis[1], lis[2], lis[3])
        except:
            return False

    def update(self, a: Test, b: Test):
        self.curs.execute(
            f"UPDATE test SET name='{b.name}',price='{b.price}', description='{b.description}' where name='{a.name}'")
        self.conn.commit()

    def delete(self, t: Test):
        self.curs.execute(f"delete from test where name='{t.name}' and price='{t.price}'")
        self.conn.commit()

    def read_all(self):
        try:
            self.curs.execute("select * from test")
            lis = self.curs.fetchall()
            test_list = []
            for i in lis:
                test_list.append(Test(i[1], i[2], i[3]))
            return test_list
        except:
            return False


class test_list_manager(DatabaseManager):
    def __init__(self):
        self.conn: connection = connect("dbname='labratoary' host='localhost' user='postgres' password='pass'")
        self.curs: cursor = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    def creat(self, t: TestList):
        try:
            self.curs.execute(f"select * from test where name='{t.test.name}'")
            t_id = self.curs.fetchone()
            t_id = t_id[0]

            self.curs.execute(f"select * from patient where national_code='{t.patient.national_code}'")
            p_id = self.curs.fetchone()
            p_id = p_id[0]

            self.curs.execute(f"select * from doctor where personal_code='{t.doctor.personal_code}'")
            d_id = self.curs.fetchone()
            d_id = d_id[0]

            self.curs.execute(
                f"INSERT INTO test_list(test_id,patient_id,doctor_id,doing_date,result_date,result) VALUES ('{t_id}','{p_id}','{d_id}','{t.doing_date}','{t.result_date}','{t.result}')")
            self.conn.commit()
        except:
            return False

    def read(self, name, national_code, doing_date):
        try:
            self.curs.execute(f"select * from test where name='{name}'")
            t_id = self.curs.fetchone()
            t_id = t_id[0]

            self.curs.execute(f"select * from patient where national_code='{national_code}'")
            p_id = self.curs.fetchone()
            p_id = p_id[0]

            self.curs.execute(
                f"SELECT * FROM test_list where test_id='{t_id}',patient_id='{p_id}',doing_date ='{doing_date}' ")
            lis = self.curs.fetchone()
            return TestList(lis[1], lis[2], lis[3], lis[4], lis[5], lis[6])
        except:
            return False

    def update(self, a: TestList, b: TestList):

        try:
            self.curs.execute(f"select * from test where name='{a.test.name}'")
            t_id = self.curs.fetchone()
            t_id = t_id[0]

            self.curs.execute(f"select * from patient where national_code='{a.patient.national_code}'")
            p_id = self.curs.fetchone()
            p_id = p_id[0]

            self.curs.execute(f"select * from doctor where personal_code='{b.doctor.personal_code}'")
            b_d_id = self.curs.fetchone()
            b_d_id = b_d_id[0]

            self.curs.execute(f"select * from test where name='{b.test.name}'")
            b_t_id = self.curs.fetchone()
            b_t_id = b_t_id[0]

            self.curs.execute(f"select * from patient where national_code='{b.patient.national_code}'")
            b_p_id = self.curs.fetchone()
            b_p_id = b_p_id[0]


            self.curs.execute(
                f"UPDATE test_list SET test_id='{b_t_id}',patient_id='{b_p_id}', doctor_id='{b_d_id}',doing_date='{b.doing_date}',result_date='{b.result_date}',result='{b.result}' where patient_id='{p_id}' and test_id='{t_id}' and doing_date = '{a.doing_date}'")
            self.conn.commit()
        except:
            return False

    def delete(self, t: TestList):
        try:
            self.curs.execute(f"select * from test where name='{t.test.name}'")
            t_id = self.curs.fetchone()
            t_id = t_id[0]

            self.curs.execute(f"select * from patient where national_code='{t.patient.national_code}'")
            p_id = self.curs.fetchone()
            p_id = p_id[0]

            self.curs.execute(f"select * from doctor where personal_code='{t.doctor.personal_code}'")
            d_id = self.curs.fetchone()
            d_id = d_id[0]

            self.curs.execute(
                f"delete from test_list where patient_id='{p_id}' and test_id='{t_id}' and doing_date = '{t.doing_date}'")
            self.conn.commit()
        except:
            return False
