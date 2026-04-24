list1 = list(map(int, input("Enter your first list :").split()))
list2 = list(map(int, input("Enter your second list :").split()))

if len(list1) != len(list2):
    print("Not a Rotation ")
    
else:

    finalList = list1 + list1
    # list1.extend(list1)  # extend list 1 as list1 + list2

    for i in range(len(list1)):
        if finalList[i:i+len(list2)] == list2 :
            print("Yes a Rotation !")
            break
    else:
        print("Not a Rotation ! ")
