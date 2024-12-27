sub1=int(input("Enter subject 1's marks: "))
sub2=int(input("Enter subject 2's marks: "))
sub3=int(input("Enter subject 3's marks: "))
sub4=int(input("Enter subject 4's marks: "))
sub5=int(input("Enter subject 5's marks: "))

sub1=int(sub1)
sub2=int(sub2)
sub3=int(sub3)
sub4=int(sub4)
sub5=int(sub5)

total=sub1+sub2+sub3+sub4+sub5
per=total/5

print(total)
print(per)

if(per>80):
    print("A grade")
elif(per>70):
        print("B grade")
elif(per>60):
      print("C grade")
elif(per>50):
      print("D grade")
elif(per>35):
      print("F grade")
else:
      print("Fail")