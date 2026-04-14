# 🔥 Q19 – Sort a List Without Using sort()

# Take numbers from user and sort them manually.
# 💡 Try:
# Bubble Sort
# Selection Sort
# (Important for interviews 👀)
print("Enter your numbers with spaces only : ",end="")
my_list = list(map(int,input().split()))
# print(f"Your entered list was : \n{my_list}")
for num_pass in range(len(my_list)):
    swapped = False
    
    for i in range(len(my_list) - num_pass - 1):

        if my_list[i] > my_list[i + 1]:
            temp = my_list[i]
            my_list[i] = my_list[i + 1]
            my_list[i + 1] = temp
            
            # my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
            #short method of swapping , tuple packing and unpacking 
            swapped = True

    if not swapped:
        break
print(my_list)