print("Enter elements in sorted order with spaces (no comma or symbol): ",end=" ")
arr = list(map(int,input().split()))

# arr = [x for x in range (1,1001)]

num = int(input("Enter element to search :"))

low = 0
high = len(arr) - 1
attempts = 0
while low <=high :
    mid = (low + high ) // 2
    # attempts +=1
    if arr[mid]==num :
        print(f"{num} is at index {mid}")
        break
    elif num > arr[mid]:
        low =mid +1
    else :
        high = mid -1
               
else:
    print("Not found !!")
# print(f"Total attempts: {attempts}")