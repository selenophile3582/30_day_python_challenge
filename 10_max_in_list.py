# 🔟 Find Maximum in a my_list
# Create a my_list of numbers and find the maximum number without using max().

my_list =[]
limit = int(input("Enter how many numbers you want to enter in the my_list :"))

for i in range (limit):
    my_list.append(int(input(f"Enter the number at index[{i}] :")))
    
largest = my_list[0]
index = 0
for i in range(limit):
    if(my_list[i]>largest):
        largest=my_list[i]
        index = i
        
print(f"The largest no. in this my_list is {largest}, at index {index}. ")