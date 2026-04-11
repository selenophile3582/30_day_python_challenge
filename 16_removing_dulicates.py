'''🔥 Q16 – Remove Duplicates from List
 Take a list from user and remove duplicate values.
 Example:
 [1, 2, 2, 3, 4, 4] → [1, 2, 3, 4]
 💡 You can try
 Using loop
 Using set (but try loop first)'''





#without using set ()O(n²)
my_list=[]
limit = int(input("How many numbers do you want to enter : "))
 
for i in range(limit):
    num=int(input(f"Enter number {i+1}: "))
    if num not in my_list:
        my_list.append(num)
    
print("List after removing duplicates is as :",my_list)





#with using set ()

# Using set() (fastest but order not guaranteed in old Python versions)
# my_list = list(set(my_list))

# Best Ordered Way (Pythonic & Clean)
# my_list = list(dict.fromkeys(my_list))
''' dist.formkeys is basically making a dictionary 
using list elements as keys and dist cannot have duplicate
kesys so  {1: None, 2: None, 3: None, 4: None}
is created and we are again converting it to list so 
order remain same '''

# ✔ Removes duplicates
# ✔ Preserves order
# ✔ Very professional way