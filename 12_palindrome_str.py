# check palindrome string (words)

my_string = input("Enter your string :")
reversed_string = my_string[::-1]

if my_string==reversed_string:
    print("Palindrome !! ")
else :
    print("Not a Palindrome !! ")
    #short method
    #print("Palindrome") if s == s[::-1] else print("Not Palindrome")


#check palindrome string (words) without considering spaces and case sensitivity
    
# my_str = input("Enter your string :")
# my_rev_str =""
# clean_str = ""
# for ch in my_str:
#     if ch.isspace():
#         continue 
#     else:
#         clean_str = clean_str + ch.lower()
#         my_rev_str = ch.lower() + my_rev_str
        
# if clean_str==my_rev_str:
#     print("Palindrome !!")
# else:
#     print("Not a Palindrome !")
        
        
        
        
#         chat gpt better solution 
        
# s = input("Enter string: ")
# clean = ""

# for ch in s:
#     if not ch.isspace():
#         clean += ch.lower()

# if clean == clean[::-1]:
#     print("Palindrome")
# else:
#     print("Not Palindrome")
