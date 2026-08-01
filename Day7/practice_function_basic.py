
#  # create funtion and to call a function
# def wellcome ():
#     print("wellcome")
# wellcome()
# print("end")


# # funtion with parameter
# def students(name):
#     print(name)
# print("this is to call to a funtion multiple time")
# students("farman")
# students("ahmad")
# students("hassanzai")


# #  function with parameter and arguments
# def city(city_name):#<--- parametre
#     print(city_name)
# city("lahore")#<---argument
# city("karachi")#<---argument


# #  functin with multiple parameter 
# def info(name,age,city):
#    print("name:",name)
#    print("age:",age)
#    print("cite:",city)
#    print("\n")
# info("farman",23,"atd")
# info("hassan",24,"lahore")
# info("ali",25,"karachi")


# # default parameter
# def student(name="unknown"):
#     print(name)
# student()


# # positional argument mean order me print karna 
# def positional(name,age):
#     print("name:",name) 
#     print("age:",age)
# positional("farman",19)

# # user input inside  function
# def add():
#     a = int(input("enter 1st number"))
#     b = int(input("enter 2nd number"))
#     c = int(input("enter 3rd number"))
#     return a+b+c
# addition = add()
# print("sum =",addition)
# print(addition)


# #  user input outside  funtion
# def add(a, b, c):
#     return a + b + c
# a = int(input("enter 1st number"))
# b = int(input("enter 2nd number"))
# c = int(input("enter 3rd number"))
# addition = add(a, b, c)
# print("sum =",addition)


# # arbitrary argument "*"
# def  students(*names):
#      print(names)
# students("farman","ahmad","hamad")


# # arbitrary argument "**"
# def  students(**details):
#      print(details)
# students(name= "ali",age= 20,city="lahore")


def add(a, b):
    return a + b

def sub(a, b):
    return a - b