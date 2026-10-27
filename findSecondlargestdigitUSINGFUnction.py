def SECONDlargest(a):
    largest=0
    secondlargest=0
    while (a>0):
        temp=a%10
        a=a//10
        if (temp>largest):
            secondlargest=largest
            largest=temp
        else :
            if (temp>secondlargest and temp!=secondlargest):
                secondlargest=temp
    return (secondlargest)
a=int(input("Enter a number:"))
print (SECONDlargest(a))