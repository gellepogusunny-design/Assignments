num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))
if num2==0:
    print("Error: Division by zero is not allowed.")
else:
    result=num1/num2
    print("The result of", num1, "divided by", num2, "is:", result)
