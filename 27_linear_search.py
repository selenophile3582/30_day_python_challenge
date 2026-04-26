# 🔥 Q27 – Implement linear Search (Without Using Built-in Functions)
# Take sorted list from user.
# Search an element using linear search.
# Print:
# Found at index X
# Not found

print("Enter your elements with spaces : ",end=" ")
user_input=list(map(int,input().split()))
num= int(input("Enter the number that you want to search : "))
index = 0
for value in user_input:
    if num ==value :
        print(f"{num} is present at index {index} or at {index + 1 } position . ")
        break
    index+=1
else:
    print("Not found ")