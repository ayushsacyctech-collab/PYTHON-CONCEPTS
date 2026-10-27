#test question 1
#n=int(input ("enter a number:"))
#i=0
#counter=0
#while (i<=n):
#    i+=1
#    if (n%i==0):
#        counter+=1
#if (counter==2):
#    print ( n,"is a prime number")
#else:
#    print ( n,"is not a prime number")


#test question 2
n=int(input ("enter a number:"))
ans=0
while (n!=0):
    ans=ans+n
    n=int(input ("enter a number:"))
print (ans)