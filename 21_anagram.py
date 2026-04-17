# 🔥 Q21 – Anagram Checker
# Take two strings from user.
# Check whether they are anagrams.
# 👉 Anagram = Same characters, different order
# Example:
# "listen" and "silent" → ✅
# "hello" and "world" → ❌
# 💡 Hint: Compare character frequency or sorted strings.

from collections import Counter 


first_word = input("Enter the first word: ")
second_word = input("Enter the second word: ")

first_word= first_word.replace(" ","").lower()
seconsecond_word=second_word.replace(" ","").lower()

if len(first_word)!=len(second_word):
    print("Not a Anagram !! ")
else :    
    print("using sort method  (n(log n ))")
    if sorted(first_word) == sorted(second_word):
        print("Anagram !! ")
    else:
        print("Not a Anagram !! ")


    print("using character frequrency")
    my_dict = {}
    for c in first_word:
        my_dict[c] = my_dict.get(c, 0) + 1

    my_sec_dict = {}
    for c in second_word :
        my_sec_dict[c] = my_sec_dict.get(c, 0) + 1

    for c in my_dict:
        if my_dict[c] != my_sec_dict.get(c,0):
            print("Not a Anagram ! ")
            break
    else:
        print("Anagram ! ")
        
    print("Using counter() , inbuilt function (O(n))")
    if Counter(first_word)==Counter(second_word):
        print("Anagram !! ")
    else :
        print("Not a Anagram !")


