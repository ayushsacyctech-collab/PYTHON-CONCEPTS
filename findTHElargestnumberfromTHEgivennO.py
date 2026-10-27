n=int(input("enter a number:"))
largest=0
while (n>0):
    temp=n%10
    n=n//10
    if (temp>largest):
        largest=temp
print (largest)