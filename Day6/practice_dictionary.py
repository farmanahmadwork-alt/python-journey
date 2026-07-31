# dictionary structure in python 
student = {"Name" : "farman Ahmad",
"Age" : 19,
"Roll No":"F25-176",
  "section/semester": "B/3rd"  }
print(student)

# access a value 
student = {"name":"ali",
"age":"22",
"marks":"78"}
print(student["age"])


# change value of key in dictionary
student = {"name":"ali",
"age":"22",
"marks":"78"}
student["age"]= "33"
print(student)


# new value add karna
student = {"name":"ali",
"age":"22",
"marks":"78"}
student["coure"]= "computer"
print(student)


# to print key
student = {"name":"ali",
"age":"22",
"marks":"78"}
student["coure"]= "computer"
print(student.keys())


# to print values
student = {"name":"ali",
"age":"22",
"marks":"78"}
student["coure"]= "computer"
print(student.values())


# use item method to print values and keys both
student = {"name":"ali",
"age":"22",
"marks":"78"}
student["coure"]= "computer"
print(student.items()) 

# loop in dictionary
student = {"name":"ali",
"age":"22",
"marks":"78"}
student["coure"]= "computer"
for key ,value in student . items():
    print(key, ":" ,value) # output
                           #  name : ali
                           #  age : 22
                           #  marks : 78
                           # coure : computer
                        
#   .pop method ude for deletion to a specific key 
student = {"name":"anas",
           "roll no":"178",
           "age":"23"}
student.pop("roll no")
print(student)


#  .popitem use for last key delete 
student = {"name":"anas",
           "roll no":"178",
           "age":"23"}
student.popitem()
print(student)


#  . clear use for all key of dictionary  but dictionary remain 
student = {"name":"anas",
           "roll no":"178",
           "age":"23"}
student.clear()
print(student)# output = {}

# . copy use for coyp of dictionary
student = {"name":"anas",
           "roll no":"178",
           "age":"23"}
student2= student.copy()
print(student2)


# samall project " srudent information system"
student = {
           "name":input("enter your name"),
           "age":int(input("enter your age")),
           "department":input("enter your department"),
           "semester":int(input("enter your semester"))
           }
print("\nstudent information system")
print(student)

# change in key 
student["semester"]= int(input("\nenter a new semester:"))

# add new key
student["cgpa"]= float(input("enter your cgpa:"))
print("\nupdated information")
print(student)