# 8️⃣ Simple Calculator
# Ask user for:
# First number
# Operator (+, -, *, /)
# Second number
# Perform the operation and print result.

first_num = float(input("Enter first number: "))
operator = input("Enter operator (+,-,*,/): ")
second_num = float(input("Enter second number: "))

if operator == '+':
    print("Result:", first_num + second_num)

elif operator == '-':
    print("Result:", first_num - second_num)

elif operator == '*':
    print("Result:", first_num * second_num)

elif operator == '/':
    if second_num == 0:
        print("Division by zero is not allowed")
    else:
        print("Result:", first_num / second_num)

else:
    print("Invalid operator")




# first_num = int(input("Enter the first number :"))
# operator = input("Enter the operaor like ( +,-,*,/ ) :")
# second_num = int(input("Enter the second number :"))

# if (operator=='+'):
#     print(f"The sum is {first_num + second_num}")
# elif (operator=='-'):
#     print(f"The difference is {first_num-second_num}") 
# elif(operator=='*'):
#     print(f'The product is {first_num*second_num}')
# elif(operator=='/'):
#     print(f"The quotient is {first_num / second_num }")
# else:
#     print("something went wrong !!")