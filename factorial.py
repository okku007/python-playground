def factorial(n):
    return 1 if(n==1 or n==0) else n * factorial(n-1)

number= int(input("Enter a number to find it's factorial: "))
print('Factorial of', number, 'is', factorial(number))