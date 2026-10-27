n=int(input("ENTER A NUMBER:"))
ans=0
if (n<0):
    num=abs(n)
else:
    num=n
while (num>0):
    reminder=num%10
    ans=ans*10+reminder
    num=num//10
if (n<0):
    print (-1*ans)
else:
    print (ans)