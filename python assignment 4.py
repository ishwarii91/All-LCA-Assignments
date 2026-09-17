rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

A = [[0] * cols for i in range(rows)]
B = [[0] * cols for i in range(rows)]
C = [[0] * cols for i in range(rows)]

print("Enter elements of Matrix A:")
for i in range(rows):
    for j in range(cols):
        A[i][j] = int(input(f"A[{i}][{j}]: "))

print("Enter elements of Matrix B:")
for i in range(rows):
    for j in range(cols):
        B[i][j] = int(input(f"B[{i}][{j}]: "))

for i in range(rows):
    for j in range(cols):
        C[i][j] = A[i][j] + B[i][j]

print("Result:")
for i in range(rows):
    print(C[i])