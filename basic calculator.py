num1 = float(input("First number:"))
num2 = float(input("Second number:"))

operator = input("Operator(+, -, *, /):")

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":    
    result = num1 * num2
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
     result = "Cannot divided by zero"
else:
      result = "invalid operator"  

print("Answer =", result)