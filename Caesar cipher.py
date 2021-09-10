# На вход программе подается строка текста на английском языке, в которой нужно зашифровать все слова. Каждое слово строки следует зашифровать с помощью шифра Цезаря (циклического сдвига на длину этого слова). Строчные буквы при этом остаются строчными, а прописные – прописными.
#
# Формат входных данных
# На вход программе подается строка текста на английском языке.
#
# Формат выходных данных
# Программа должна вывести зашифрованный текст в соответствии с условием задачи.
#
# Примечание. Символы, не являющиеся английскими буквами, не изменяются.
#
# Тестовые данные 🟢
# Sample Input 1:
#
# Day, mice. "Year" is a mistake!
# Sample Output 1:
#
# Gdb, qmgi. "Ciev" ku b tpzahrl!
# Sample Input 2:
#
# my name is Python!
# Sample Output 2:
#
# oa reqi ku Veznut!


alpha1 = "abcdefghijklmnopqrstuvwxyz"
alpha2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

text = input()
text = text.split(' ')
result = ""
for m in text:
    m = str(m)
    l = 0
    for j in m:
        if j in alpha1 or j in alpha2:
            l += 1

    for i in m:
        if i.isalpha():
            if i.islower() == True:
                k = ord(i) + l
                if k > 122:
                    k = k - 122 + 96
                    result += chr(k)
                else:
                    result += chr(k)
            else:
                k = ord(i) + l
                if k > 90:
                    k = k - 90 + 64
                    result += chr(k)
                else:
                    result += chr(k)
        else:
            result += i
    result += " "
print(result)
