# 💡 Practice nested loops.
# 🔥 Q24 – Matrix Transpose
# Take a matrix and print its transpose.
# Example:
# Original:
# 1 2 3
# 4 5 6
# Transpose:
# 1 4
# 2 5
# 3 6


rows = int(input("Enter the numbers of rows : "))
cols = int(input("Enter the numbers of cols : "))

matrix = []

for i in range(rows):
    while True :
        print(f"Enter row {i+1} with space-separated values:",end=" ")
        row=list(map(int,input().split()))
        if len(row)== cols:
            matrix.append(row)
            break 
        else:
            print("Enter exactly", cols, "elements.")

print("The transposed matrix is : ")

for i in range(cols):
    for j in range(rows):
        print(f"{matrix[j][i]}",end=" ")
    print()
print("-----")