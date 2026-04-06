# Take a number as input and check whether it is a palindrome or not.

num = int(input("Enter number: "))

if num < 0:
    print("Negative numbers are not palindrome")
else:
    original = num
    rev = 0

    while num > 0:
        rev = rev * 10 + num % 10
        num //= 10

    if original == rev:
        print("Palindrome")
    else:
        print("Not Palindrome")
