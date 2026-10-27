n=int(input("enter a number:"))

print ("==========ODD===============")
sum=0
for i in range (1,n+1):
    if (i%2==1):
        sum+=i

print(sum)

print ("===========EVEN==============")
sum=0
for i in range (1,n+1):
    if (i%2==0):
        sum+=i
print(sum)