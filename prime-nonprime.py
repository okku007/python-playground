number=int(input("Enter a number to check if it's a prime number or not: "))

if number == 0 or number == 1:
    print(number, "is not a prime number")
elif number > 1:
    for i in range(2,number):
        if(number % i) == 0:
            print(number,"is not a prime number")
            break
    else:
            print(number,"is a prime number")
else:
    print(number,"is not a prime number")