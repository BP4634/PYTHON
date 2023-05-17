
print("***Welcome to our Restaurant***")
print("\nHere is our menu:\n")

bill = 0

menu = {"pizza":300,"chicken":350,"steak":600,"pasta":450,"cold drink":100}
cart_selection = {}


for i in menu:
    print(i + ": $" + str(menu[i]))

repeat = False
p = False
T = True
backup = 0

while T == True:
    
    if repeat == False:

        order = input("\nWhat would you like to order? Press Enter after your input to continue.\n")
        
    else:
        
        order = input("\nWhat else would you like to order? Press Enter after your input to continue. \n")

    for k in menu:   

        if order.lower().rfind('stop') > -1:
            T = False
            print("\nYour order is: \n")
            for j in cart_selection:
                print(j,"("+str(cart_selection[j])+")")
           
            print("\nyour total bill is: "+str(bill))
            print("\n*****Thanks for ordering at our Restaurant*****\n")
            break
            


        elif order.lower().rfind(k) > -1:
            p = True
            quantity = int(input(f"\nHow many serves of {k} would you like? Press Enter after your input to continue. \n"))
            bill = bill + menu[k]*quantity

            if k in cart_selection.keys():
                cart_selection[k] = quantity + cart_selection.get(k)
            else:

                cart_selection[k] = quantity
            repeat = True
            


    if p == False:
        print("\nService not available. Please, select a valid option: \n")
        for i in menu:
            print(i + ": $" + str(menu[i]))
            
    
    
        