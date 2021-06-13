from core.manager import *
from psycopg2 import connect
from psycopg2._psycopg import connection, cursor
from user.models import *


class Adimn_Manager(DatabaseManager):
    def __init__(self):
        self.conn: connection = connect("dbname='labratoary' host='localhost' user='postgres' password='pass'")
        self.curs: cursor = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    def creat(self, a: Admin):
        self.curs.execute(f"INSERT INTO admin(username,password) VALUES ('{a.username}','{a.password}')")
        self.conn.commit()

    def read(self, username, password):
        try:
            self.curs.execute(f"SELECT * FROM admin where username='{username}' and password='{password}'")
            lis = self.curs.fetchone()
            return Admin(lis[1], lis[2])
        except:
            return False

    def update(self, a: Admin, b: Admin):
        self.curs.execute(
            f"UPDATE admin SET username='{b.username}',password='{b.password}' where username='{a.username}' and password='{a.password}' ")
        self.conn.commit()

    def delete(self, a: Admin):
        self.curs.execute(f"delete from admin where username='{a.username}' and password='{a.password}'")
        self.conn.commit()


class Doctor_Manager(DatabaseManager):
    def __init__(self):
        self.conn: connection = connect("dbname='labratoary' host='localhost' user='postgres' password='pass'")
        self.curs: cursor = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    def creat(self, d: Doctor):
        self.curs.execute(
            f"INSERT INTO doctor(first_name,last_name,personal_code,password) VALUES ('{d.first_name}','{d.last_name}','{d.personal_code}','{d.password}')")
        self.conn.commit()

    def read(self, personal_code, password):
        try:
            self.curs.execute(f"SELECT * FROM doctor where personal_code='{personal_code}' and password='{password}'")
            lis = self.curs.fetchone()
            return Doctor(lis[1], lis[2], lis[3], lis[4])
        except:
            return False

    def update(self, f_d: Doctor, s_d: Doctor):
        self.curs.execute(
            f"UPDATE doctor SET first_name='{s_d.first_name}',last_name='{s_d.last_name}',personal_code='{s_d.personal_code}'"
            f",password='{s_d.password}' where personal_code='{f_d.personal_code}' and password='{f_d.password}' ")
        self.conn.commit()

    def delete(self, d: Doctor):
        self.curs.execute(f"delete from doctor where personal_code='{d.personal_code}' and password='{d.password}'")
        self.conn.commit()


class Patient_Manager(DatabaseManager):
    def __init__(self):
        self.conn: connection = connect("dbname='labratoary' host='localhost' user='postgres' password='pass'")
        self.curs: cursor = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    def creat(self, p: Patient):
        self.curs.execute(
            f"INSERT INTO patient(first_name,last_name,national_code,phone_number,birth_date) VALUES ('{p.first_name}','{p.last_name}','{p.national_code}','{p.phone_number}','{p.birth_date}')")
        self.conn.commit()

    def read(self, phone_number, national_code):
        try:
            self.curs.execute(
                f"SELECT * FROM patient where national_code='{national_code}' and phone_number='{phone_number}'")
            lis = self.curs.fetchone()
            return Patient(lis[1], lis[2], lis[3], lis[4], lis[5])
        except:
            return False

    def update(self, f_p: Patient, s_p: Patient):
        self.curs.execute(
            f"UPDATE patient SET first_name='{s_p.first_name}',last_name='{s_p.last_name}',national_code='{s_p.national_code}'"
            f",phone_number='{s_p.phone_number}',birth_date='{s_p.birth_date}' where national_code='{f_p.national_code}' and phone_number='{f_p.phone_number}' ")

        self.conn.commit()

    def delete(self, p: Doctor):
        self.curs.execute(
            f"delete from patient where national_code='{p.national_code}' and phone_number='{p.phone_number}'")
        self.conn.commit()

