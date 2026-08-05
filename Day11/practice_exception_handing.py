# # exception handing


# # 1 try exception
# #--->jaha error malaoom na ho

# try:
#     num1 = int(input("Enter First Number: "))
#     num2 = int(input("Enter Second Number: "))

#     print("Answer =", num1 / num2)

# except:

#     print("Second number cannot b zero(0)")



# #specific exception/value error
# #---->Jab tum alag alag error ke liye alag message dena chahte ho.
# try:
#       age=int(input("enter age"))

#       print("Student Registered")

# except ValueError:
      
#       print("Age must be  number")




# # zero division error
# #-->Jab kisi number ko zero se divide karte hain.
# try:
#     total_marks = 500

#     students = int(input("Number of students: "))

#     average = total_marks / students

#     print("Average =", average)

# except ZeroDivisionError:

#     print("Number of students cannot be zero.")



# #IndexError
# #-->Jab list me jo index mang rahe ho woh exist hi nahi karta.
# try:

#     fruits = ["Apple", "Mango", "Banana"]

#     print(fruits[5])

# except IndexError:

#     print("Index does not exist.")# output-->Index does not exist.




# # KeyError
# #-->Dictionary me key nahi mile. 
# account = {

#     "name": "Ali",
#     "balance": 50000
# }

# try:
#     print(account["pin"])

# except KeyError:

#     print("PIN information not found.")



# #file not founder
# #  -->Jab file exist hi na kare.
# try:
#     file = open("students.txt", "r")

#     data = file.read()

#     print(data)

#     file.close()

# except FileNotFoundError:
#     print("Student file does not exist.")



# # Multiple Except
# # -->Ek se zyada errors ane k chances hon osko alag alag handle karna.
# try:
#     amount = int(input("Enter Amount: "))

#     print(10000 / amount)

# except ValueError:
#     print("Amount must be a number.")

# except ZeroDivisionError:
#     print("Amount cannot be zero.")




# # else
# #-->Ye tab chalega jab koi error na aaye. try block code me
# try:
#     age=int(input("enter age"))

# except ValueError:
#     print("Age must be number")

# else:
#     print("student registered successfully")




# #finally
# # -->Ye har hal me chalta hai.Chahe error aaye ya na aaye.
# try:
#     num = int(input("Enter Number: "))
#     print(10 / num)

# except ZeroDivisionError:
#     print("Cannot divide by zero.")

# finally:
#     print("Program End")





# #raise
# # Khud apni error banana
# amount = int(input("Enter Amount: "))

# if amount < 100:
#     raise ValueError("Minimum withdrawal is 100.")

# print("Transaction Successful.")
class InvalidAgeError(Exception):
    pass

age = int(input("Enter Age: "))

if age < 18:
    raise InvalidAgeError("Age must be 18 or above.")

print("Registration Successful")




#Custom Exception
#Apni khud ki error class banana.




# # except Exception as e
# # Jab error aaye to us error ko ek variable me store kar lete hain.
# try:
#     a = int(input("First Number: "))
#     b = int(input("Second Number: "))

#     print(a / b)

# except Exception as e:
#     print("Error:", e)
