
'''
# if ststement
print("this is if ststement")
age = 18
if age >= 18:
    print("you can adult")

age = 68
if age >= 60:
    print("you become old")  

name = "faimii"
if name == "faimii":
    print("wellcomr faimii")


    # if else statement
    print("..................")
    print("this is  else if ststement")
age = 18
if age >= 18:
    print("you can adult")
else:
    print(not adult)

age = 68
if age >= 60:
    print("you become old")  
else:
    print(not old)

name = "faimii"
if name == "faimii":
    print("wellcomr faimii")
else:
    print("bye faimii")  

print("..................")
print("this is if-elif-else ststement")  
marks =int(input("enter youyr marks"))
if marks >=90 and marks < 100 :
    print("A+")
elif marks >=80 and marks<90:
    print("B+")
elif marks >=70 and marks <80:
    print("C+")
else:
    print("fail")

# nested if statements
print("..................")
print("this is nested if ststement")  
age = int(input("enter your age"))
has_licence = input("do you have licence? (true/false):")
if age >=18:
    if has_licence == "true":
        print("you drive the car")
else:
    print("you need to drive a car")

    # match if ststement
print("..................")
print("this is match if statement") 
choice = int(input("enter a choice"))
match choice:
    case 1:
        print("monday")
    case 2:
        print("tuesday")
    case 3:
         print("wednesday")
    case 4:
         print("thursday")
    case 5:
        print("friday")
    case 6:
        print("saturday")
    case 7:
         print("sunday")
    case _:
         print("default day")

         '''

pin = input("Enter PIN: ")

if pin == "1234":

    balance = 10000

    print("1. Check Balance")
    print("2. Withdraw Money")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            print("Balance =", balance)

        case 2:
            amount = int(input("Enter amount: "))

            if amount <= balance:
                balance -= amount
                print("Withdraw Successful")
                print("Remaining Balance =", balance)
            else:
                print("Insufficient Balance")

        case 3:
            print("Thank You!")

        case _:
            print("Invalid Choice")

else:
    print("Wrong PIN")

    







  

    



    












