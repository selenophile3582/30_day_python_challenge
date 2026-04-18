# 🔥 Q22 – Longest Word in a Sentence

# Take a full sentence from user.
# Find the longest word.
# Example:
# "I love Python programming"
# Output → "programming"
# hint = we use .split() for words and list for char 

sen = input("Enter your sentence ")
sentence = sen.split()

if  not sentence:
    print("No word entered !! ")
else :
    largest_word = sentence[0]
    for words in sentence :
        if len(words) > len(largest_word):
            largest_word=words  
            
    print(f"The largest word in this sentence is  \"{largest_word}\"")

# now better version
input_sentence = input("Enter your sentence : ")
sentence_words = input_sentence.split()

if sentence_words :
    print("Longest word : ", max(sentence_words,key=len))  #this find max of the length 
else :
    print("No words entered !! ")
