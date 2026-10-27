def smallestDIGIT(a):
    smallest=999999
    while(a>0):
        temp=a%10
        a=a//10
        if (temp<smallest):
            smallest=temp
    return smallest
a=int(input("Enter a number for a:"))
print (smallestDIGIT(a))