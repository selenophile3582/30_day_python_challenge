num = int(input("Enter number: "))

if num <= 1:
    print("Not prime")
else:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print("Composite")
            break
    else:
        print("Prime")


# num = int(input("Enter the number :"))

# l=[]
# isprime=0
# if(num<1):
#     print("Please enter a valid natural number")

# elif(num==1):
#     print("1 is neither prime nor composite number .")

# elif(num==2):
#     print(" 2 is the only even prime number .")
# else:
#     for i in range(2,num):
#         if(num%i==0):
#             l.append(i)
#             isprime=1
#     if(isprime):
#          print(f"{num} is a composite number and is divisible by {l}")

#     else:
#         print("The given number is a prime number . ")
