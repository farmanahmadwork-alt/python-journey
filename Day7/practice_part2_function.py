# normaly function 
def add(a, b):
    return a + b
print(add(10, 20))# 30


#lambda in function
add = lambda a,b:a+b
print(add(10,20))# 30


# square in lambda
square = lambda x,y :x*x and y * y
print(square(5,6))


# mul* in lambda
mul1 = lambda x,y:  x * y 
mul2 = lambda  w,z:  w * z
print(mul1(10,5))
print(mul2( 3,5))


# recursion in function
def hello(n):
    if n==0:
        return 0
    print(n)
    hello(n-1)
hello(10)


# local variable mean  isnide function but not outside
def student ():
    name = "farman"
    print(name)
student()


# global variable  mean  outside and inside both function
name = "ali"
def student():
    print(name)
student()
print(name)


# global variable  can b change inside function
name = "ali"
def student():
    name ="faimii"
student()
print(name)


# modules in function 
def add(a,b):
    return a + b
print(add(4,5))

def sub(a,b):
    return a - b
print(sub(4,5))

def mul(a,b):
    return a * b
print(mul(4,5))

def div(a,b):
    return a / b
print(div(4,5))


# import modelus for to connect two file 
import practice_function_basic

print(practice_function_basic.add(10, 20))
print(practice_function_basic.sub(20, 5))
