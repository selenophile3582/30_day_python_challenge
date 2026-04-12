#counting the characte frequency


my_str = input("Enter your string :")

my_dict = {}

for c in my_str:
    # if c in my_dict:
    #     my_dict[c]+=1
    # else :
    #     my_dict[c]=1
    
    my_dict[c]=my_dict.get(c,0) + 1
    
#my_dict['spaces']=my_dict.pop(" ",None)
if " " in my_dict:
    # my_dict["spaces"]=my_dict[" "]     
    # del my_dict[" "]
   ##more cleaner version   
    my_dict["spaces"]=my_dict.pop(" ")
    
print(my_dict)




# professional way using (counter form collections )
# Time com... is still (0)n, but more professional

from collections import Counter

my__str = input("Enter your string :")

freq = Counter(my__str)
print(freq)   #it prints in desceding order of freqency 
# print(dict(freq))  #it prints in the order , as input is entered
print(freq.most_common(2))  # 2 here is telling to print 2 most comoon characters 


#using defaultdict from collections 

from collections import defaultdict

my_str_def_dict = input("Enter your string: ")

freq = defaultdict(int)

for c in my_str_def_dict:
    freq[c] += 1

print(dict(freq))
# print((freq)) #defaultdict (<class 'int'>,)