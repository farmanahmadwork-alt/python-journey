balance = 50000
pin = "5566"

def verify_pin():

    user_pin = input("Enter Your Pin:")
    if user_pin==pin:
      print("login successfully")
      return True
    else:
       print("invalid pin")
       return False

def menu():

    print("=======Wellcome To ATM Machine========")
    print("1.Check balance")
    print("2.Deposit Money")
    print("3.Withdraw money")
    print("4.Enter Pin")
    print("5.Exit")
    print("==========================")

def check_balance():
    print(f"your current balance is :{balance}")

def deposite():
    global bakance

    amount = int(input("enter deposite amount:"))
    balance = balance + amount

    print(f"{amount} deposited successfully")
    print(f"current balance:{balance}")


def withdraw():
    global balance 

    amount=int(input("enter withdraw amount"))
    if amount <= balance:

        balance = balance - amount

        print(f"{amount} withdraw successfully:")
        print(f"current balance :{balance}")

    else :
        print("insufficient balance:")


def change_pin():
    global pin 


    old_pin=input("enter old pin:")
    if old_pin==pin:

        new_pin=input("enter your new pin")
        pin= new_pin

        print("pin change successfully:")

    else:
        print("incorrect old pin:")


if verify_pin == False:
    exit()

while True:
    menu()

    choice = input("Enter Your Choice:")

    if choice == "1":
        check_balance()

    elif choice == "2":
        deposit()

    elif choice == "3":
        withdraw()

    elif choice == "4":
        change_pin()

    elif choice == "5":
        print("Thank You For Using ATM")
        break

    else:
        print("Invalid Choice")


