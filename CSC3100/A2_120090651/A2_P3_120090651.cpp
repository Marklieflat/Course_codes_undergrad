#include <iostream>
#include <cmath>
using namespace std;

char arr[2200][2200];
void carpet(int n, int x, int y);

void carpet(int n, int x, int y) {
    if (n == 1) {
        arr[x][y] = ' ';
        arr[x-1][y-1] = '#';
        arr[x-1][y] = '#';
        arr[x-1][y+1] = '#';
        arr[x][y-1] = '#';
        arr[x][y+1] = '#';
        arr[x+1][y-1] = '#';
        arr[x+1][y] = '#';
        arr[x+1][y+1] = '#';
        return;
    }
    int len = (int)pow(3, n);
    int l = ((len/3)-1)/2;
    for (int i = x-l; i <= x+l; i++) {
        for (int j = y-l; j <= y+l; j++) {
            arr[i][j] = ' ';
        }
    }
    carpet(n-1, x-len/3, y-len/3);
    carpet(n-1, x-len/3, y);
    carpet(n-1, x-len/3, y+len/3);
    carpet(n-1, x, y-len/3);
    carpet(n-1, x, y+len/3);
    carpet(n-1, x+len/3, y-len/3);
    carpet(n-1, x+len/3, y);
    carpet(n-1, x+len/3, y+len/3);
}

int main() {
    int n;
    cin >> n;
    int len = (int)pow(3, n);
    int mid = (len - 1) / 2;
    carpet(n, mid, mid);
    for (int i = 0; i < (int)pow(3, n); i++) {
        for (int j = 0; j < (int)pow(3, n); j++) {
            cout << arr[i][j];
        }
        cout << endl;
    }
}