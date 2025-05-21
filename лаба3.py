# 26. Формируется матрица F следующим образом: 
# Скопировать в нее матрицу А и если сумма чисел по периметру области 1 больше, чем количество нулей по периметру области 4, то поменять симметрично области 1 и 3 местами, иначе 1 и 2 поменять местами несимметрично. При этом матрица А не меняется. После чего вычисляется выражение:((К*AT)*А)-K*FT . Выводятся по мере формирования А, F и все матричные операции последовательно.
from copy import deepcopy
def deterministic_generator(seed, N):
    matrix = []
    for i in range(N):
        row = []
        for j in range(N):
            val = (seed + i * N + j) % 21 - 10
            row.append(val)
        matrix.append(row)
    return matrix
def print_matrix(matrix, title="Matrix"):
    print(f"{title}:")
    for row in matrix:
        print(" ".join(f"{elem:4}" for elem in row))
    print()
def sum_perimeter_region1(matrix, N):
    half = N // 2
    total = 0
    total += sum(matrix[0][:half])
    for i in range(1, half):
        total += matrix[i][half-1]
    if N % 2 == 1:
        total += sum(matrix[half][:half])
    else:
        for i in range(half):
            total += matrix[half-1][i]
    for i in range(1, half):
        total += matrix[i][0]
    return total
def count_zeros_perimeter_region4(matrix, N):
    half = N // 2
    count = 0
    for i in range(half, N):
        if matrix[i][0] == 0:
            count += 1 
    if N % 2 == 1:
        for j in range(1, half):
            if matrix[N-1][j] == 0:
                count += 1
    else:
        for j in range(1, half):
            if matrix[N-1][j] == 0:
                count += 1
    for i in range(N-1, half, -1):
        if matrix[i][half-1] == 0:
            count += 1
    return count
def swap_regions_1_3_symmetrical(F, N):
    half = N // 2
    for i in range(half):
        for j in range(half):
            F[i][j], F[N - 1 - i][j] = F[N - 1 - i][j], F[i][j]
def swap_regions_1_2_asymmetrical(F, N):
    half = N // 2
    for i in range(half):
        for j in range(half):
            if N % 2 == 0:
                F[i][j], F[i][j + half] = F[i][j + half], F[i][j]
            else:
                F[i][j], F[i][j + half + 1] = F[i][j + half + 1], F[i][j]
def transpose_matrix(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
def multiply_matrices(A, B):
    n = len(A)
    return [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
def multiply_matrix_by_scalar(matrix, scalar):
    return [[elem * scalar for elem in row] for row in matrix]
def subtract_matrices(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def main():
    K = int(input("Введите K: "))
    N = int(input("Введите N: "))
    seed = 42  
    A = deterministic_generator(seed, N)
    print_matrix(A, "Исходная матрица A")
    F = deepcopy(A)
    sum_r1 = sum_perimeter_region1(A, N)
    zeros_r4 = count_zeros_perimeter_region4(A, N)
    print(f"Сумма по периметру области 1: {sum_r1}")
    print(f"Количество нулей по периметру области 4: {zeros_r4}")
    if sum_r1 > zeros_r4:
        print("Сумма области 1 > нулей области 4, меняем 1 и 3 симметрично")
        swap_regions_1_3_symmetrical(F, N)
    else:
        print("Сумма области 1 <= нулей области 4, меняем 1 и 2 несимметрично")
        swap_regions_1_2_asymmetrical(F, N)   
    print_matrix(F, "Матрица F после преобразований")
    AT = transpose_matrix(A)
    print_matrix(AT, "A^T")
    K_AT = multiply_matrix_by_scalar(AT, K)
    print_matrix(K_AT, "K*A^T")
    K_AT_A = multiply_matrices(K_AT, A)
    print_matrix(K_AT_A, "(K*A^T)*A")
    FT = transpose_matrix(F)
    print_matrix(FT, "F^T")
    K_FT = multiply_matrix_by_scalar(FT, K)
    print_matrix(K_FT, "K*F^T")
    result = subtract_matrices(K_AT_A, K_FT)
    print_matrix(result, "Результат ((K*A^T)*A) - K*F^T")
if __name__ == "__main__":
    main()
