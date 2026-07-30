
# jion method in string
names = ["farman", "ali", "hamad"]
print(" ".join(names))

# no spaces
names = ["f","a","r","m","a","n"]
print("".join(names))

 # isalpha() method ye check karta he k code me only alphabates he ya nahi
 # agr number,space ho to to false 
name = "python"
print(name.isalpha())

# isdigit() method ye check karta he k code me only digits he ya nahi
 # agr letter,space ho to to false 
name = "1235"
print(name.isdigit())

# isalnum() method ye check karta he k code me only alphabates and number he ya nahi
 # agr space ho to  false 
name = "1235farman"
print(name.isalnum())

# isspace() method ye check karta he k code me only space he ya nahi
 # agr letter,digits ho to to false 
name = "  "
print(name.isspace())



# escape character 
# \n use for next line
name = "faimii"
print("hello\n" +name)


name = input("enter name")
age = input("enter age")
print(f"name:{name}\nt age :{age}")



# double backslash " \\ " for actual print man jo code me hoga 
print("c:farman\\ahmad")# c:farman\ahmad

# use \t tabe for make list
print("name\tage")
print("wahaj\t23")
print("farooq\t34")

# f-string
name= "faimii"
age = 23
print(f"hello my name is {name} and i am {age} year old.")# hello my name is faimii and i am 23 year old.

name = "faimii"
print(f"hello {name}")

# practice question
name= "faimii"
age = 23
print(f" {name} is {age} year old")

a = 30
b = 10
print(f"sum = {a+b}")

city = input("enter city")
print(f" welcome to {city}")

name = input("enter name")
course = input("enter cours")
print(f" student name is : {name}")
print(f"course is : {course}")


 # format method
name = input("enter name:")
age = input("enter age:")
print(" my name is {} and i am {} year old.".format(name, age))







