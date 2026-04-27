# 28. Prime Numbers in Range
# Print primes within a given range.

limit = int(input("Enter your limit :"))

for i in range(2,limit+1):
    isPrime = True
    for j in range(2,int(i**0.5)+1):
        if i % j == 0 :
            isPrime = False
            break
    if isPrime:
        print(i , end=" ")