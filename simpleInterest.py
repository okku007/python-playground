def simpleInterest(p,n,r):
    return (p*n*r)/100

principleAmount= int(input("Enter the principle amount: "))
interestRate = int(input("Enter the interest rate: "))
numberofYear = int(input("Enter the number of time (in year): "))

print('Total interest is: ', simpleInterest(principleAmount,interestRate,numberofYear))