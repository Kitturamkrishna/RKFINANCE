import mysql.connector as connector
import datetime as date
import logging
class User :

    dates1 = date.datetime.now()
    name = "RKFINANCE"
    def __init__(self):
        self.con = connector.connect(host='localhost',
                                     user='root',
                                     password='root',
                                     database='RKFINANCE')

    def create(self, name, phone, DOB, Address, LOAN,interest, password,total):
        query = "insert into customers(name,phone,DOB,Address,LOAN,Interest,password,total)values('{}',{},'{}','{}',{},'{}','{}',{})".format(
            name, phone, DOB, Address, LOAN,interest, password,total)
        # print(query)
        curr = self.con.cursor()
        curr.execute(query)
        self.con.commit()
        print("Account created  successfully at  ", self.dates1)

    def find_customer(self, account_no):
        query = "select * from customers where userid ={}".format(account_no)
        cur = self.con.cursor()
        cur.execute(query)
        res = cur.fetchall()
        if res:
            for row in res:
                print("Account number  : ", row[0])
                print("name  : ", row[1])
                print("phone number  : ", row[2])
                print("DOB  : ", row[3])
                print("Address  : ", row[4])
                print(" balance   : ", row[5])
                print(" balance   : ", row[6])
                print(" balance   : ", row[7])
                print(" balance   : ", row[8])
                print()
                print()
        else:
            print("USER DOESNT EXIST ! PLEASE TRY WITH VALID ACCOUNT ")

    def delete_customer(self, account_no):
        q = "select * from customers where userid = {}".format(account_no)
        curr = self.con.cursor()
        curr.execute(q)
        res = curr.fetchall()
        if res:
            query = "delete from customers where userid = {}".format(account_no)
            cur = self.con.cursor()
            cur.execute(query)
            res = cur.fetchone()
            self.con.commit()
            print("Your Account is deleted Successfully at  ", self.dates1)
            print()
        else:
            print("ACCOUNT DOESNT EXIST ! PLEASE TRY WITH VALID ACCOUNT")

    def update_customer(self, account_no):
        q = "select * from customers where userid = {}".format(account_no)
        curr = self.con.cursor()
        curr.execute(q)
        res = curr.fetchall()
        if res:
            newName = input("enter newname : ").capitalize()
            while True:
                newphone = int(input('enter your phone number : '))
                if len(str(newphone)) > 10 or len(str(newphone)) < 10:
                    print("Invalid phone number ! please enter 10 digit only ")
                else:
                    break
            newaddress = input("enter newaddress : ").capitalize()
            query = "update customers set name = '{}' , phone = {} , Address = '{}' where userid= {} ".format(
                newName, newphone, newaddress, account_no)
            cur = self.con.cursor()
            cur.execute(query)
            self.con.commit()
            print("Account details updated successfully  at ", self.dates1)
        else:
            print("ACCOUNT DOESNT EXIST ! PLEASE TRY WITH VALID ACCOUNT")

    def returnmoney(self,acc_no):
        query = "select * from customers where userid ={}".format(acc_no)
        cur = self.con.cursor()
        cur.execute(query)
        res = cur.fetchone()
        n = len(res)
        if res :
            q = 'select total from customers where userid = {}'.format(acc_no)
            curr = self.con.cursor()
            curr.execute(q)
            res1 = curr.fetchone()

            print("your balance is : " , res[8])
            return_amt = int(input("enter amount you want to return "))
            remaining_amt = int(res1[0]) - return_amt
            qu = "update customers set total = {} where userid = {}".format(remaining_amt,acc_no)
            currr = self.con.cursor()
            currr.execute(qu)
            self.con.commit()
            print("money returned successfully and updated ")
        else :
            print("user not found")





