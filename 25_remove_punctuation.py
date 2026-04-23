import string

myStr = input("Enter your string : ")
pun = string.punctuation

clearStr = "".join([c for c in myStr if c not in pun])

# for c in myStr:
#     if c in pun:
#         continue
#     else:
#         clearStr.append(c)

print("".join(clearStr))
