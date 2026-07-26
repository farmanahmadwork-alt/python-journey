# structure or array 
marks = [10,20,30,40,50]
print(marks) #ouput will be 10,20,30,40,50,

#  in programing index start frome 0 not from 1
marks = [10,20,30,40,50]
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])# ouput will be 10,20,30,40,50,

# to print what value onn index 2
print(marks[2])# output 30

# negative index in which index starts from righ  or opposite side 
print(marks[-2])# output 40

# change value of index index
marks = [10,20,30]
marks[1]= 80
print(marks)# output [10, 80, 30]

#add new value 
marks = [10,20,30]
marks.append(70)
print(marks)#output [10, 20, 30, 70]

# remove value
marks = [10,20,30,70]
marks.remove(70)
print(marks)#output [10, 20, 30, ]

# find lenth of array
marks = [10,20,30,70]
print(len(marks))# output 4

 # delete list item
marks = [10,20,30,70]
marks.pop()
print(marks) #  [10,20,30] becuse pop delete last value

# reverse list value
marks = [10,20,30,70]
marks.reverse()
print(marks)# output[70, 30, 20, 10]


marks =[30,10,70,20,40]
marks.sort()
print(marks)# output [10, 20, 30, 70]mean sequence me value lana

# how much time 10 are present in list
marks = [30,10,70,20,10,40,10]
print(marks.count(10))# output 3 time

# to check 70 is on which index
marks = [30,10,"70",20,40]
print(marks)
print(marks.index("70"))# output index 2 


