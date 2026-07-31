# structure of set 
# set  not follow order for printing
structure_set = {"oppo","samsung","vivo","i_phone"}
print(structure_set)


# dupicate in set automatically remove
duplicate = {"10","20","10","30","20","40","50"}
print(duplicate)


# different datatype
datatype = {"faimii",34,3.5,"is true"}
print(datatype)


#  type of set
datatype = {"faimii",34,3.5,"is true"}
print(type(datatype))


# indexing in set not allowed
#index = {"23","34","56","7","8","90"}
#print(index[3]) # output error {TypeError: 'set' object is not subscriptable}


# part two starts
# add ,remove ,update , discard'remove,pop,
# add in set
add = {"apple","babnana","mango"}
add.add("grapes")
print(add)


# remove  and discard behave same in set 
remove = {"apple","banana","mango","grapes"}
remove.remove("grapes")
print(remove)


# update use for multiple value at a time
update = {"apple","banana","mango","grapes"}
update.update(["orange","pine_apple"])
print(update)

# remove random value
pop = {"apple","banana","mango","grapes"}
pop.pop()
print(pop)

# parts 3 in set
# union,intersection,difference,symmetric_difference,clear,copy,

# union mean return all value and duplicate remove
set1 = {1,2,3,4,5}
set2 = {2,4,6,6,7}
print(set1.union(set2))# output{1, 2, 3, 4, 5, 6, 7}


# intersection mean return only commen value
set1 = {1,2,3,4,5}
set2 = {2,4,6,6,7}
print(set1.intersection(set2))# {2, 4}


# difference mean return only those value whose set1 value are  not present in set2
set1 = {1,2,3,4,5,6}
set2 = {2,4,6,6,7}
print(set1.difference(set2))#  {1, 3, 5}


# symmetric_difference mean return wich are not machin both
set1 = {1,2,3,4,5,6}
set2 = {2,4,6,6,7}
print(set1.symmetric_difference(set2))# {1, 3, 5, 7}


# clear mean delete all value
set1 = {1,2,3,4,5,6}
set1.clear()
print(set1)# set()


# copy mean creat copy 
set = {23,45,67,89,10}
new_set= set.copy()
print(new_set)# {67, 23, 89, 10, 45}

# d/f b/w list,set,dictionary,tuples
'''
Python Collection Types Difference Table
Feature	      List	           Tuple	              Set	        Dictionary
Symbol	       []	             ()	                   {}	        {key:value}
Ordered    	✅ Yes	           ✅ Yes	            ❌ No       	✅ Yes (Python 3.7+)
Changeable	✅ Yes	           ❌ No	                ✅ Yes	    ✅ Yes
Duplicate 	✅ Allowed	       ✅ Allowed         	❌ Not       ❌ Duplicate Keys Not Allowed
Indexing    ✅ Yes	           ✅ Yes	            ❌ No	    ❌ Keys se access hota hai
Mutable	    ✅ Yes	           ❌ No	                ✅ Yes	    ✅ Yes
   
'''