#tuple - (), ordered, unchangeable, indexed

a = (1,2,3,4,5)

b = "hi",2,3,4,5,4.2

c = [10,8,9,5]

c[2] = 788

#a[2] = 987 -> impossible to change

print(b)
print(a[2])
print(c[2])
print(b[1:3])


fruits = ("apple","banana","mango","banana","banana","banana","mango","mango")

#fruit1,fruit2,fruit3 = fruits    #UNPACKING METHOD


#print(fruit3)

print(fruits.count("mango"))
print(fruits.index("banana"))




print(dir(tuple))





