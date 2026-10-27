n=int(input("Enter a number:"))
counter=0
for i in range (1,n+1):
    if (i%5==0):
        counter+=1
print (counter)