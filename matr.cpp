/* 
По данным числам n и m заполните двумерный массив размером n×m числами от 1 до n×m по спирали, выходящей из левого верхнего угла и закрученной по часовой стрелке, как показано в примере.
Формат входных данных
Вводятся два числа n и m, не превышающие 100.

Формат выходных данных
Выведите полученный массив, отводя на вывод каждого элемента ровно 4 символа.

Sample Input:

4 5
Sample Output:

   1   2   3   4   5
  14  15  16  17   6
  13  20  19  18   7
  12  11  10   9   8

*/

#include <iostream>
#include <iomanip>
using namespace std;
int main() {
    int n, m, i, j, nom = 2, p = 20;
    int a[100][100];
    cin >> n >> m;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            a[i][j] = -1;
        }
    }
    i = 0;
    j = 0;
    a[0][0] = 1;
    for (int f = 0; f < p; f++) {
        while (a[i][j + 1] == -1) {
            a[i][j + 1] = nom;
            nom += 1;
            j += 1;
        }
        while (a[i + 1][j] == -1) {
            a[i + 1][j] = nom;
            nom += 1;
            i += 1;
        }
        while (a[i][j - 1] == -1) {
            a[i][j - 1] = nom;
            nom += 1;
            j -= 1;
        }
        while (a[i - 1][j] == -1) {
            a[i - 1][j] = nom;
            nom += 1;
            i -= 1;
        }
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cout << setw(4) << a[i][j];
        }
        cout << endl;
    }


    // put your code here
    return 0;
}