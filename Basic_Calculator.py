


print("..........................BASIC CALCULATOR.........................................")
print("                                            ")
print("                                            ")


valid=False

while not(valid):


    a=int(input("Enter the first number:"))


    print("                                            ")


    print("Press 1 for addition")
    print("Press 2 for substraction")
    print("Press 3 for multiplication")
    print("Press 4 for division")
    print("Press 5 for power")
    print("Press 6 for root")
    C=int(input(":"))



    print("                                            ")
    print("                                            ")

    b=int(input("Enter the second number:"))

    print("                                            ")
    print("                                            ")




    
    if C==1:
        R=a+b
        print(R)
        valid=True

    elif C==2:
        R=a-b
        print(R)
        valid=True

    elif C==3:
        R=a*b
        print(R)
        valid=True

    elif C==4:
        R=a/b
        print(R)
        valid=True

    elif C==5:
        R=pow(a,b)
        print(R)
        valid=True

    elif C==6:
        R=pow(a,(1/b))
        print(R)
        valid=True

    else:
        print("Please enter a valid option")
        



