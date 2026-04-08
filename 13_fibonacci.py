# Print first n Fibonacci numbers.

n = int(input("Enter the number of terms  :"))

#  loop method
a = 0
b = 1
print("This is using loops ",end="-> ")
for i in range(n):
    print(a,end=" ")
    a,b=b,a+b # here its same as temp = a , a = b and b = a+b
    #this method is good for memory 
    
print("")
#recursion method but it is slow and memory issue
print("This is using recursion ",end="-> ")
def fib (num):
    return num if num <= 1 else fib(num-1) + fib(num-2)
        
for i in range(0,n ):
    print(fib(i),end=" ")