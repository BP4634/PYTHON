
                                                               #BEFORE ChatGPT:



num = int(input(print("\nEnter a number\n")))

flag = False
if num == 1:
    print(num, "is not a prime number")
elif num > 1:
    for i in range(2,num):
        if (num % i) == 0:
            flag = True

            break

if flag:
    print(num, "is not a prime number")

else:
    print(num, "is a prime number")





                                                     #AFTER ChatGPT:

number = int(input(print("\nEnter a number\n")))

if all(number % i != 0 for i in range (2, num)):
    print(number, "is a prime number")
else:
    print(number, "is not a prime number")
