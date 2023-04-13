from User import User
from Owner import Admin

print()
print("  WELCOME TO  " , User.name)
user = User()
admin = Admin()
print()
inp = input("please enter admin or user  ")

if inp == 'user'  :
       while True :

          print()
          print("Enter 1 to create an Userid ")
          print("Enter 2 to display your Userid details  ")
          print("Enter 3 to delete your Userid  ")
          print("Enter 4 to update  your Useridad ")
          print("Enter 5 to return money  ")
          print("enter 6 to break ")
          print()

          try :
              choice = int(input())
              if choice == 1:

                  name = input('please enter your name : ')
                  while True :
                    phone = int(input('enter your phone number : '))
                    if len(str(phone)) > 10 or len(str(phone)) < 10 :
                      print("Invalid phone number ! please enter 10 digit only ")
                    else :
                        break
                  DOB = input('please enter you date of birth ')
                  Address = input('enter your address : ')
                  while True :
                     loan = int(input("please enter loan amount : "))
                     if loan <= 0 :
                         print('loan amount cant be zero ')
                     else :
                         break
                  months = int(input("enter how many months you want"))
                  interest = loan*Admin.ROI*months//100




                  while True :
                    password = input('please enter password ')
                    if len(str(password)) <= 5 or len(str(password)) >= 18 :
                        print("Enter passwword greater than 5 and less than 18 char ")
                    else : break

                  total = interest + loan

                  user.create(name,phone,DOB,Address,loan,interest,password,total)
              elif choice == 2 :
                  usr = int(input("enter userid"))
                  user.find_customer(usr)
              elif choice == 3:
                  usr = int(input("enter user id to delete account "))
                  user.delete_customer(usr)
              elif choice == 4 :
                  usr = int(input("enter user id to update your details "))
                  user.update_customer(usr)
              elif choice == 5 :
                  usr = int(input("enter user id to update your details "))
                  user.returnmoney(usr)
              else :
                  print("Thank you for using RK Finance ")
                  break

          except Exception as e :
              print(e)
elif inp == 'admin':
        # while True:
          username = input('please enter username : ')
          password = input('pleasse enter password')
          if username != admin.admin and password != admin.password:
              print("please enter correct credentials ")
          else :
           while True :
             print()
             print("Enter 1 to display  all customers  ")
             print("Enter 2 to display a specific customer  ")
             print("Enter 3 to delete an  account ")
             print("Enter 4 to update  an  account ")
             print("Enter 5 to delete all customers ")
             print("Enter 6 to complete an transactions ")
             print()
             try :
                choice = int(input('please enter your choice to perform operations '))

                if choice == 1:
                   admin.showall_customers()
                elif choice == 2 :
                   inp = int(input("please enter Userid to fetch customer details : "))
                   admin.find_customer(inp)
                elif choice == 3 :
                   inp = int(input("please enter Userid to delete customer  : "))
                   admin.delete_customer(inp)
                elif choice == 4 :
                   cid = int(input("please enter Userid to update your details "))
                   admin.update_customer(cid)
                elif choice == 5:
                   admin.deleteAllcustomers()
                elif choice == 6 :
                   print("Thank you admin ! see you soon ")
                   break
                else :
                   print("Invalid input ! try again ")
             except Exception as e :
               print(e)
               print("invalid details ! try again ")


