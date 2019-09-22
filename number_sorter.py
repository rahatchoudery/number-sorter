//ask the user for three numbers
x = input("What is your first number? ")
x = int(x)

y = input("What is your second number? ")
y = int(y)

z = input("What is your third number? ")
z = int(z)


//display the smallest number
if (x <= y) and (x <= z):
    print ("\nThe smallest number is", x)

elif (y <= x) and (y <= z):
    print("\nThe smallest number is", y)
    
else:
    print("\nThe smallest number is", z)
    
//display the middle number    
if ((x <= y) and (x >= z)) or ((x >= y) and (x <= z)):
    print ("The middle number is", x)
    
elif ((y <= x) and (y >= z)) or ((y >= x) and (y <= z)):
    print("The middle number is", y)

else:
    print("The middle number is", z)
    
    
//display the largest number
if (x >= y) and (x >= z):
    print ("The largest number is", x)

elif (y >= x) and (y >= z):
    print("The largest number is", y)
    
else:
    print("The largest number is", z)
