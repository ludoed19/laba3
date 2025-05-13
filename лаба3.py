# 26. Формируется матрица F следующим образом: 
# Скопировать в нее матрицу А и если сумма чисел по периметру области 1 больше, чем количество нулей по периметру области 4, то поменять симметрично области 1 и 3 местами, иначе 1 и 2 поменять местами несимметрично. При этом матрица А не меняется. После чего вычисляется выражение:((К*AT)*А)-K*FT . Выводятся по мере формирования А, F и все матричные операции последовательно.
def print_matrix(matrix, title):
    print(title)
    for row in matrix:
        print(' '.join(f"{elem:4}" for elem in row))
    print()
def generate_matrix(N):
    return [[i*N + j + 1 for j in range(N)] for i in range(N)]
def get_part_perimeter_sum(matrix, part):
    N = len(matrix)
    if part == 1:  
        return sum(matrix[0])
    elif part == 4:  
        return sum(row[0] for row in matrix)
    return 0
def get_part_perimeter_zero_count(matrix, part):
    N = len(matrix)
    if part == 4: 
        return sum(1 for row in matrix if row[0] == 0)
    return 0
def swap_parts_symmetrical(F, N):
    mid = N // 2
    part1 = [row[:mid] for row in F[:mid]]
    part3 = [row[mid + (N%2):] for row in F[mid + (N%2):]]
    for i in range(mid):
        for j in range(mid):
            F[i][j] = part3[mid-1-i][mid-1-j]
    for i in range(mid + (N%2), N):
        for j in range(mid + (N%2), N):
            F[i][j] = part1[N-1-i][N-1-j]
    return F
def swap_parts_asymmetrical(F, N):
    mid = N // 2
    part1 = [row[:mid] for row in F[:mid]]
    part2 = [row[mid:] for row in F[:mid]] 
    for i in range(mid):
        F[i][:mid] = part2[i]
        F[i][mid:] = part1[i]
    return F
def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
def matrix_multiply(A, B):
    n = len(A)
    m = len(A[0])
    p = len(B[0])
    return [[sum(A[i][k] * B[k][j] for k in range(m)) for j in range(p)] for i in range(n)]
def matrix_scalar_multiply(matrix, scalar):
    return [[scalar * elem for elem in row] for row in matrix]
def matrix_subtract(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def main():
    K = int(input("Введите число K: "))
    N = int(input("Введите размер матрицы N: "))
    if N < 2:
        print("Ошибка: N должно быть ≥ 2")
        return
    A = generate_matrix(N)
    print_matrix(A, "A:")
    F = [row.copy() for row in A]
    sum_part1 = get_part_perimeter_sum(A, 1)
    zero_count_part4 = get_part_perimeter_zero_count(A, 4)
    print(f"Сумма по периметру области 1: {sum_part1}")
    print(f"Количество нулей по периметру области 4: {zero_count_part4}")
    if sum_part1 > zero_count_part4:
        print("Условие выполнено: меняем области 1 и 3 симметрично")
        F = swap_parts_symmetrical(F, N)
    else:
        print("Условие не выполнено: меняем области 1 и 2 несимметрично")
        F = swap_parts_asymmetrical(F, N)
    print_matrix(F, "F:")
    AT = transpose(A)
    print_matrix(AT, "A^T:")
    K_AT = matrix_scalar_multiply(AT, K)
    print_matrix(K_AT, "K * A^T:")
    K_AT_A = matrix_multiply(K_AT, A)
    print_matrix(K_AT_A, "(K * A^T) * A:")
    FT = transpose(F)
    print_matrix(FT, "F^T:")
    K_FT = matrix_scalar_multiply(FT, K)
    print_matrix(K_FT, "K * F^T:")
    result = matrix_subtract(K_AT_A, K_FT)
    print_matrix(result, "((K * A^T) * A) - K * F^T:")
if __name__ == "__main__":
    main()
