def minimum(number1,number2,number3):
    smallest=min(number1,number2,number3)
    return smallest
    
def maximum(num1,num2,num3):
        largest=max(num1,num2,num3)
        return largest
    

    
n1=int(input("Enter 1st number: "))
n2=int(input("Enter 2nd number: "))
n3=int(input("Enter 3rd number: "))



print("The largest number is: ", maximum(n1,n2,n3))
print("The smallest number is: ", minimum(n1,n2,n3))