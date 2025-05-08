def matrix_generator(K, N):
    for i in range(N):
        row = []
        for j in range(N):
            val = (K * i + j) % 21 - 10 
            row.append(val)
        yield row
K = int(input("K: "))
N = int(input("N: "))
A = [row for row in matrix_generator(K, N)]
print("A:")
for row in A:
    print(row)
part_1 = []  
part_2 = []  
part_3 = []  
part_4 = []  
for i in range(N):
    for j in range(N):
        if i < j and i + j < N - 1:
            part_1.append(A[i][j])  
        elif i < j and i + j > N - 1:
            part_2.append(A[i][j])  
        elif i > j and i + j > N - 1:
            part_3.append(A[i][j])  
        elif i > j and i + j < N - 1:
            part_4.append(A[i][j])  
print("\n 1:", part_1)
print(" 2 :", part_2)
print(" 3 :", part_3)
print(" 4 :", part_4)
def print_matrix(matrix, name):
    print(f"\n {name}:")
    for row in matrix:
        print(row)
F = [row[:] for row in A]
def min_in_odd_columns(matrix, N):
    min_elements = []
    for j in range(1, N, 2):  
        for i in range(N):
            if i < j and i + j > N - 1: 
                min_elements.append(matrix[i][j])
    return min_elements.count(min(min_elements)) if min_elements else 0
def max_in_even_rows(matrix, N):
    max_elements = []
    for i in range(0, N, 2): 
        for j in range(N):
            if i < j and i + j < N - 1:  
                max_elements.append(matrix[i][j])
    return max_elements.count(max(max_elements)) if max_elements else 0
min_count = min_in_odd_columns(A, N)
max_count = max_in_even_rows(A, N)
if min_count > max_count:
    for i in range(N):
        for j in range(N):
            if i < j and i + j < N - 1:  
                if i < j and i + j > N - 1:  
                    F[i][j], F[N - j - 1][N - i - 1] = F[N - j - 1][N - i - 1], F[i][j]
else:
    for i in range(N):
        for j in range(N):
            if i < j and i + j > N - 1:  
                if i > j and i + j > N - 1:  
                    F[i][j], F[i][j] = F[i][j], F[i][j]

def multiply_matrices(A, B, N):
    return [[sum(A[i][k] * B[k][j] for k in range(N)) for j in range(N)] for i in range(N)]
def transpose_matrix(A, N):
    return [[A[j][i] for j in range(N)] for i in range(N)]
A_squared = multiply_matrices(A, A, N)
A_transposed = transpose_matrix(A, N)
K_A_transposed = [[K * A_transposed[i][j] for j in range(N)] for i in range(N)]
Final_Result = [[A_squared[i][j] + K_A_transposed[i][j] for j in range(N)] for i in range(N)]
print_matrix(F, "F")
print_matrix(A_squared, "A * A")
print_matrix(K_A_transposed, "K * A^T")
print_matrix(Final_Result, "A * A + (K * A^T)")
