# selection sort
import sys

my_list = list(map(int, input("Enter the numbers with spaces only").split()))

for num_pass in range(len(my_list)):
    milestone = sys.maxsize

    for i in range(num_pass, len(my_list)):
        if milestone > my_list[i]:
            milestone = my_list[i]
            index = i

    my_list[num_pass], my_list[index] = my_list[index], my_list[num_pass]

print(f"my list after sorting \n{my_list}")
