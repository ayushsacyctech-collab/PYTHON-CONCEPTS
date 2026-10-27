def swipe(a,b):
    a=a+b
    b=a-b
    a=a-b
    return(a,b)
a=int(input("Enter a number for a:"))
b=int(input("Enter a number for b:"))
print (swipe(a,b))