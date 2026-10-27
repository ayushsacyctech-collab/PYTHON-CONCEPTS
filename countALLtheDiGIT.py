n=int(input("enter a number:"))
count=0
if (n<0):
    num=abs(n)
else:
    num = n

while (num>0):
    num=num//10
    count+=1


print(count)