# 5️⃣ Count Vowels
# Take a stringing from the user and count how many vowels it contains.

my_string = input("Enter your string : ")
vowels = 0
my_string=my_string.lower()
for i in range(len(my_string)):
    if my_string[i]=='a' or my_string[i]=='e' or my_string[i]=='i' or my_string[i]=='o' or my_string[i]=='u':
        vowels +=1

print(f"The numbers of vowels is {vowels}")


#trying with list of vowels 
count =0
vowels_list =['a','e','i','o','u']
# for i in range(len(my_string)):
for ch in my_string :
    if ch in vowels_list:
        count  +=1
        
print(f"The numbers of vowels is {count } using a list of vowels .")

#gpt answer 
# vowels_set = {'a','e','i','o','u'}

# count = 0
# for ch in my_string.lower():
#     if ch in vowels_set:
#         count += 1

# print(count)
