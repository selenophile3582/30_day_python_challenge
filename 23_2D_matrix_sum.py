print("Enter your first 2D matrix : ")
matrix1=[ [0]*2 for i in range(2)]
matrix2=[ [0]*2 for i in range(2)]


for i in range(2):
    for j in range(2):
        matrix1[i][j]=int(input(f"Enter number at position [{i}][{j}]: "))
       
print("Enter the elements of matrix 2nd : ") 
for i in range(2):
    for j in range(2):
        matrix2[i][j]=int(input(f"Enter number at position [{i}][[{j}]]: "))
print("The sum of the matrix is :")
for i in range(2):
    for j in range(2):
        print(f"{matrix1[i][j] + matrix2[i][j]}",end=" ")
    print()