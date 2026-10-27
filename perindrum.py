num=int(input("enter  NUMBER : "))
ans=0
n=num
while (n>0):
    reminder=n%10
    ans=ans*10+reminder
    n=n//10
if (num==ans):
    print ("true")
else:
    print ("false")