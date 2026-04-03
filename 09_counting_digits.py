# Take a number and count how many digits it has.
# Example:
# 12345 → 5 digits

num = abs(int(input("Enter the number :")))
print(f"The no. of digit is {len(str(num))}")  #method 1st 
digit = 0
if(num==0):
    print("The number of digits is 1 ")
else:
    while (num>0):
        num//= 10
        digit+=1
    
print(f"The no. of digit is {digit}")
