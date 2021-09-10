# На вход программе подается натуральное число nn. Напишите программу, которая выводит первые nn строк треугольника Паскаля.
#
# Формат входных данных
# На вход программе подается число n \, (n \ge 1)n (n≥1).
#
# Формат выходных данных
# Программа должна вывести первые nn строк треугольника Паскаля, каждую на отдельной строке в соответствии с образцом.
#
# Тестовые данные 🟢
# Sample Input 1:
#
# 4
# Sample Output 1:
#
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# Sample Input 2:
#
# 5
# Sample Output 2:
#
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1
# Sample Input 3:
#
# 2
# Sample Output 3:
#
# 1
# 1 1


trian = [[1], [1, 1]]
n = int(input())
if n == 1:
    print(1)
elif n == 2:
    print(1)
    print(1, 1)
elif n >= 3:
    for j in range(1, n - 1):
        newlist = [1]
        for i in range(len(trian[j])-1):
            newlist.append(trian[j][i] + trian[j][i+1])
        newlist.append(1)
        trian.append(newlist)
    for m in trian:
        a = ""
        for k in m:
            a += str(k) + " "
        print(a)