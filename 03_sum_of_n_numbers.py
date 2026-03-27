print("This program will print the sum of natural numbers up to the entered number . ")
num = int(input("Enter the number : "))
total = 0
for i in range(1,num+1):
    total += i
    
print(f"The sum of natural numbers till {num} is {total}.")

total_using_formula = num * (num +1) //2
print("The sum with formula is : ",total_using_formula)


'''
sum_of_natural numbers = (n * (n+1))  // 2 
   // for floor division , calculates in one go 
   so reduce time 

'''
 
 