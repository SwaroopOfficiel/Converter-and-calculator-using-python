
num1=float(input("Enter the first number:"))
op=input("Enter Operator:")
num2=float(input("Enter the second number:"))
if op == "+":
    print(num1+ num2)
elif op == "-":
    print(num1-num2)
elif op == "*":
    print(num1*num2)
elif op == "/":
    print(num1/num2)
else:
    print("Invaild operator")
# odd and even number
num = int(input("Enter the number:"))
if (num % 2) == 0:
    print("{0} is even number", format(num))

else:
    print("{0} is odd number", format(num))