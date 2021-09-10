# Напишите программу, которая перемножает две матрицы.
#
# Формат входных данных
# На вход программе подаются два натуральных числа nn и mm — количество строк и столбцов в первой матрице, затем элементы первой матрицы, затем пустая строка. Далее следуют числа mm и kk — количество строк и столбцов второй матрицы затем элементы второй матрицы.
#
# Формат выходных данных
# Программа должна вывести результирующую матрицу, разделяя элементы символом пробела.
#
# Тестовые данные 🟢
# Sample Input 1:
#
# 2 2
# 1 2
# 3 2
#
# 2 2
# 3 2
# 1 1
# Sample Output 1:
#
# 5 4
# 11 8
# Sample Input 2:
#
# 3 2
# 2 5
# 6 7
# 1 8
#
# 2 3
# 1 2 1
# 0 1 0
# Sample Output 2:
#
# 2 9 2
# 6 19 6
# 1 10 1
# Sample Input 3:
#
# 3 3
# 2 4 6
# 1 3 5
# 0 4 8
#
# 3 3
# 6 3 1
# 9 6 3
# 0 2 0
# Sample Output 3:
#
# 48 42 14
# 33 31 10
# 36 40 12



inp1 = input().split()
n, m = int(inp1[0]), int(inp1[1])
lst = []
lst1 = []
lst2 = []
for _ in range(n):
    lst.append(input().split())
storka = input()
inp2 = input().split()
l, k = int(inp2[0]), int(inp2[1])
for _ in range(l):
    lst1.append(input().split())
for i in range(n):
    lst2.append([])
    for j in range(k):
        lst2[i].append(0)
for i in range(n):
    for j in range(k):
        summa = 0
        for x in range(m):
            lst2[i][j] += int(lst[i][x]) * int(lst1[x][j])
for i in range(n):
    print(*lst2[i])


