#to store more than a single value, we need collection data types

#list-> represented with square brackets, indexed, duplicate, operations can be performed
#tuple-> 
#dict->represented with curly brackets, we use it to store data in key value pairs
#set->



                                                                #LIST EXAMPLES

a = ["apple", "banana", "mango", 1, 74, 36]

#print(a[0])
#print(a[1])
#print(a[2])
#print(a[5])


#print(a[0:6])

#print(a[0:5:2])


x = 5,6

#print(x)

a[3] = "Cherry"

#print(a)



mylist = [1,2,3,4,5,4,4,4,4,4,4,2,3,4,5,4,4,4,4,4,4]
disorder = [8,4,6,3,2,4,9,1,5,8]
b = ["a", "b"]
mylist.extend(b)
mylist.insert(4,"Bryan")
mylist.pop(3)
mylist.remove(2)
mylist.remove('b')
mylist.reverse()
disorder.sort()


b = mylist.copy()

mylist.append(6)

print(mylist)

print(mylist.count(4))

print(mylist.index(5))

mylist.clear()


print(mylist)

print(b)
print(disorder)

print(dir(list))





                                                     #DICTIONARY EXAMPLES







w = {"Model":"Iphone13","price": 60000,"Quality":"High quality",5:17}

print(w["Model"])
print(w["price"])
print(w["Quality"])
print(w[5])
print(w)

student = dict(name = "Bryan", roll = 12, standard = 11, city = "D.R.")

print(student["city"])
print(student['name'])
print(student["roll"])
print(student['standard'])
print(student)

student['school'] = "NYC"
print(student)

keys_students = list(student.keys())
values_students = list(student.values())



print(student.keys())

print(keys_students)
print(values_students)

student.update(name = "John")


print(student)

j = student.items()
print(j)

i = ["name", "city"]

t = dict.fromkeys(i)

print(t)

t.update(name = "BP")

print(t)


print(" ")
print(" ")
print(" ")

print(values_students[2])

print(" ")
print(" ")
print(" ")





print(dir(dict))


