# Напишите программу для вычисления суммы двух матриц.
#
# Формат входных данных
# На вход программе подаются два натуральных числа nn и mm — количество строк и столбцов в матрицах, затем элементы первой матрицы, затем пустая строка, далее следуют элементы второй матрицы.
#
# Формат выходных данных
# Программа должна вывести результирующую матрицу, разделяя элементы символом пробела.
#
# Тестовые данные 🟢
# Sample Input 1:
#
# 2 4
# 1 2 3 4
# 5 6 7 1
#
# 3 2 1 2
# 1 3 1 3
# Sample Output 1:
#
# 4 4 4 6
# 6 9 8 4
# Sample Input 2:
#
# 3 3
# 9 6 3
# 3 1 1
# 4 7 5
#
# 0 3 2
# 1 7 8
# 4 2 3
# Sample Output 2:
#
# 9 9 5
# 4 8 9
# 8 9 8
# Sample Input 3:
#
# 1 1
# 1
#
# 1
# Sample Output 3:
#
# 2



s = input().split()
n, m = int(s[0]), int(s[1])
lst = []
lst1 = []
lst2 = []
for _ in range(n):
    lst.append(input().split())
stroka = input()
for _ in range(n):
    lst1.append(input().split())
for i in range(n):
    lst2.append([])
    for j in range(m):
        lst2[i].append(int(lst[i][j]) + int(lst1[i][j]))
    print(*lst2[i])


