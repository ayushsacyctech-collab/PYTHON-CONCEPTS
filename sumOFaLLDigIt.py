n=int(input("Enter a number:"))
ans=0
while (n>0):
    temp=n%10
    ans=temp+ans
    n=n//10
if (ans>10):
    n=ans
    ans = 0
    while (n>0):
        temp=n%10
        ans=temp+ans
        n=n//10
    print(ans)
else:
    print (ans)