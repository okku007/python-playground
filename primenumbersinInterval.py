numberRange1=int(input("Enter range 1: "))
numberRange2=int(input("Enter range 2: "))

print("Prime numbers between", numberRange1, "and", numberRange2, "are: ")

for i in range(numberRange1, numberRange2 + 1):
    if i>1:
        for j in range(2,i):
            if(i % j)==0:
                break
        else:
            print(i)