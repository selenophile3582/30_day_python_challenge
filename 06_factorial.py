def fact(n):
    if n == 0 or n ==1 :
        return n
    return n * fact(n-1)

num = int(input("Enter number: "))

if num < 0:
    print("Factorial not defined for negative numbers")
else:
    factorial = 1
    for i in range(2, num+1):
        factorial *= i

    print("Iterative:", factorial)
    print("Recursive:", fact(num))
