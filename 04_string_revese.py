my_string = input("Enter your word that you want to reverse :")
result = ""
for i in range (len(my_string)):
    result = my_string[i] + result

print(result)


# more pythonic Way 
text = input("Enter word: ")
print(text[::-1])
