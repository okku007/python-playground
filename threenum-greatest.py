x=int(input("Enter number 1: "))
y=int(input("Enter number 2: "))
z=int(input("Enter number 3: "))

if(x>y):
    print("num1 is greater than num2")
elif(x>z):
    print("num1 is greater than num3")

if(y>x):
    print("num2 is greater than num1")
elif(y>z):
    print("num2 is greater than num3")

if(z>x):
    print("num3 is greater than num1")
elif(z>y):
    print("num3 is greater than num2")