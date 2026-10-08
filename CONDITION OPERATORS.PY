num1=int(input("Enter a number for num1:"))
num2=int(input("Enter a number for num2:"))
multiply=int(input("Enter a number to multiply:"))
if (num1>num2):
    print(num1,"is greater")
    print(num2 ,"x", multiply," = ",num2*multiply)

elif num1<num2:
    print(num2,"is greater")
    print(num1 ,"x", multiply," = ",num1*multiply)

else: 
    print(num1, " == ", num2)