# constructor

class Student:

    def __init__(self):
        print("Student object created")


s1 = Student()
s2 = Student()


class Car:

    def __init__(self):
        print("Car object created")


car1 = Car()
car2 = Car()



class Laptop:

    def __init__(self):
        print("Laptop object created")


l1 = Laptop()
l2 = Laptop()


class Student:

    def __init__(self):
        self.name = "Farman"
        self.age = 21
        self.marks = 85
        self.city = "Abbottabad"

    def show_data(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Marks:", self.marks)
        print("City:", self.city)


s1 = Student()
s1.show_data()


class Car:

    def __init__(self):
        self.name = "Mercedes"
        self.color = "Black"
        self.model = 2025

    def start(self):
        print(self.name, "is starting...")


car1 = Car()

print("Name:", car1.name)
print("Color:", car1.color)
print("Model:", car1.model)

car1.start()



class BankAccount:

    def __init__(self):
        self.account_holder = "Farman"
        self.balance = 50000

    def show_balance(self):
        print("Account Holder:", self.account_holder)
        print("Balance:", self.balance)


account1 = BankAccount()

account1.show_balance()


