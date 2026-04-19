print("This program will find the sum of 2 2D matrix of any no of rows and column ")
rows = int(input("Enter the numbers of rows : "))
coloums = int(input("Enter the numbers of columns : "))
matrix1=[]
matrix2=[]


for i in range(rows):
    print(f"Enter the element of row {i +1 } with spaces :", end=" ")
    row = list(map(int,input().split()))
    if len(row)!=coloums:
        print("Invalid input ! again run the program and enter properly ! ")
    else:
      matrix1.append(row)  

print("Enter the elements of matrix 2nd : ") 
for i in range(rows):
    print(f"Enter the element of row {i +1 } with spaces  :",end=" ")
    row = list(map(int,input().split()))
    if len(row)!=coloums:
        print("Invalid input ! again run the program and enter properly ! ")
    else:
        matrix2.append(row)
    
print("The sum of the matrix is :")
for i in range(rows):
    for j in range(coloums):
        print(f"{matrix1[i][j] + matrix2[i][j]}",end=" ")
    print()