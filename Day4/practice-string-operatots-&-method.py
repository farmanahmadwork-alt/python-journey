
# operator in string
# cancatenation operator " + "

str1 = "farman"
str2 = "ahmad"
print(str1 + " " + str2 )

# repetition operator
name  =  "farman"
print((name + " ")* 5)


# in And  not in operator 
# in opert
name  =  "farman"
print("r"in name)# true either false

# not in opert
name  =  "farman"
print("r" not in name)# true either false

# in opert practice question?
email = input("enter email")
if "@" in email :
    print("valid email")
else:
    print("invalid email")

# method in string
 # upper case

name = "farman"
print(name . upper())

 # lower case

name = "FARMAN"
print(name . lower())
\

#title mean  every words of firts  leter  becom capital
name ="hello! my name is farman ahmad"
print(name.title())

 #swapcase mean lower become upper and upper become lower
name ="hElLo! my naMe is fArMan aHmADd"
print(name.swapcase())

# in this condition do not change original string
name = "farman"
name.upper()
print(name)


# in this condition  change original string
name = "farman"
name =name.upper()
print(name)

# capatelized mean first letter become capital
name = "hello! my name is farman ahmad"
print(name.capitalize())


# pracrice question

sentence = " i love pakistan"
print(sentence.lower())

sentence = "i love pakistan"
print(sentence . title())

name = "PyThOn"
name =name.swapcase()
print(name)

# strip mean ye spacec ko remove karta he 
fruit = "   mango  "
print(fruit.strip())
# without strip
fruit = "   mango  "
print(fruit)

# replace the words to another mean instead of java print python
subject = "i love java"
print(subject.replace("java","python"))

alphabates = "a lave  an mura"
print(alphabates.replace("a","i"))


#Find method to find  of letter on which index and when not 
#found  print negative index 
name = "farman"
print(name.find("m"))

# to find any letter how much time are present like " a " 
name = "farman"
print(name.count("a"))#2

# practise Question  

text = "python"
print(text.find("z"))# output -1  
#print(text.index("z"))# error 

# start swith to check a  is string starts from sepecific words
text =  input("enter text").strip()
words = input("enter words").strip()
print(text.startswith(words))


# end swith to check a  is string end on sepecific words
text =  input("enter text").strip()
#words = input("enter words").strip()
end_word = input("enter end words").strip()
if text.endswith(end_word): 
    print(" text end with" ,end_word)



# split method in string mean one string is split into multiple
name = "farman ali hamad"
print(name.split())# output['farman', 'ali', 'hamad']

