# На вход программе подаются два натуральных числа nn и mm. Напишите программу, которая создает матрицу размером n \times mn×m заполнив её "спиралью" в соответствии с образцом.
#
# Формат входных данных
# На вход программе на одной строке подаются два натуральных числа nn и mm — количество строк и столбцов в матрице.
#
# Формат выходных данных
# Программа должна вывести матрицу в соответствии образцом.
#
# Примечание. Для вывода элементов матрицы как в примерах, отводите ровно 33 символа на каждый элемент. Для этого используйте строковый метод ljust(). Можно обойтись и без ljust(), система примет и такое решение 😇
#
# Тестовые данные 🟢
# Sample Input 1:
#
# 4 5
# Sample Output 1:
#
# 1  2  3  4  5
# 14 15 16 17 6
# 13 20 19 18 7
# 12 11 10 9  8
# Sample Input 2:
#
# 1 6
# Sample Output 2:
#
# 1  2  3  4  5  6
# Sample Input 3:
#
# 3 3
# Sample Output 3:
#
# 1  2  3
# 8  9  4
# 7  6  5


s = input().split()


def proverka(matrix):
    flag = True
    for b in matrix:
        if "." in b:
            flag = False
            break
    return flag


n, m = int(s[0]), int(s[1])
lst = []
for i in range(n):
    lst.append([])
    for j in range(m):
        lst[i].append(".")
lst[0][0] = "1"
stroka = 0
ryad = 0
count = 1
flag = False
while not flag:
    while ryad + 1 < m and lst[stroka][ryad + 1] == ".":
        count += 1
        lst[stroka][ryad + 1] = count
        ryad += 1
    while stroka + 1 < n and lst[stroka + 1][ryad] == ".":
        count += 1
        lst[stroka + 1][ryad] = count
        stroka += 1
    while ryad - 1 > -1 and lst[stroka][ryad - 1] == ".":
        count += 1
        lst[stroka][ryad - 1] = count
        ryad -= 1
    while stroka - 1 > -1 and lst[stroka - 1][ryad] == ".":
        count += 1
        lst[stroka - 1][ryad] = count
        stroka -= 1
    flag = proverka(lst)
for a in lst:
    print(*a)


