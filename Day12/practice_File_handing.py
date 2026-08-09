# File Handing


# 1 File . open
# use for to open a file 
file = open("student.txt", "w")
print("File opened successfully")



# close mode
# use for to close a file
file = open("student.txt", "w")
file.write("Hello Python")
file.close()#--->close mode



# file .read
# use for to read a file
file = open("student.txt", "r")
data = file.read()
print(data)



# write mode
# use for to enter new data but old data automatically deleted
file = open("student.txt", "w")
file.write("Name: Ali")
file.close()



# append mode
# use for a new data at the end
file = open("student.txt", "a")
file.write("\nAge: 22")
file.close()



# X mode
# use for create a new file
file = open("newfile.txt", "x")
file.write("Hello")
file.close()



# readline mode
# use for to read one line at a time
file = open("student.txt", "r")
line1 = file.readline()
print(line1)
file.close()


#with open() mode
# use for closed file without write close mode
with open("student.txt", "w") as file:
    file.write("Hello")



# tell mode
# File ke andar cursor ki current position batana.   
with open("student.txt", "r") as file:
    print("Starting position:", file.tell())
    file.read(6)
    print("Current position:", file.tell())



# seek mode
# File ke cursor ko kisi specific position par le jana.Cursor ko file ke bilkul start par le jao.
with open("student.txt", "r") as file:
    print("First:", file.read(5))
    file.seek(0)
    print("Again:", file.read(5))



# r+ mode mean read + write
# use for read and write a file
with open("student.txt", "r+") as file:
    data = file.read()
    print(data)
    file.write("\nNew Data")


# w+ mode mean write + read
# use for to write and read a file but old data chances be deleted
with open("student.txt", "w+") as file:
    file.write("Hello Python")
    file.seek(0)
    print(file.read())  



# a+ mode mean append + read 
# use for read and add new data at the end
with open("student.txt", "a+") as file:
    file.write("\nNew Student")
    file.seek(0)
    print(file.read())



#  strip mode
# strip() string ke beginning aur ending ke unnecessary whitespace/newline ko remove karta hai.
with open("student.txt", "r") as file:
    line = file.readline()
    print(line.strip())



# binary mode
# rb mean read binary mode and use for read binary data
with open("image.jpg", "rb") as file:
    data = file.read()
print(data)


# wb mean write binary and use for write binary dat in file
with open("copy.jpg", "wb") as file:
    file.write(data)



# ab mean append binry 
# use for add  binary data at the end 
with open("file.bin", "ab") as file:
    file.write(data)



#  Encoding mode
#Encoding ek rule hai jo batata hai:
# "Text ke characters ko computer ke bytes me kaise store karna hai aur wapas characters me kaise read karna hai."
with open("data.txt", "w", encoding="utf-8") as file:
    file.write("السلام علیکم")




