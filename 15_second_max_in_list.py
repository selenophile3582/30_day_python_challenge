# Q15 – Find Second Largest Number in a List
# Take list input from user.
# Find the second largest element without using sort() or max().

import sys

limit = int(input("How many numbers you want to enter: "))

if limit < 2:
    print("At least 2 numbers are required.")
else:
    my_list = []
    
    for i in range(limit):
        num = int(input(f"Enter number {i+1}: "))
        my_list.append(num)

    largest = second = -sys.maxsize - 1

    for num in my_list:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num

    if second == -sys.maxsize - 1:
        print("No second largest number (all numbers may be equal).")
    else:
        print("Second largest number is:", second)



# import sys
# limit = int(input("How many numbers you want to enter :"))
# my_list = []
# print(f"Enter your {limit} numbers :", end=" ")
# for i in range(limit):
#     my_list.append(int(input()))

# largest=my_list[0]

# for i in my_list :
#     if i > largest:
#         largest=i
        
# sec_max = -sys.maxsize - 1
# for item in my_list :
#     if ( sec_max < item and sec_max < largest ):
#        if (item != largest):
#          sec_max = item
        
# print("The second largest number is :",sec_max)


