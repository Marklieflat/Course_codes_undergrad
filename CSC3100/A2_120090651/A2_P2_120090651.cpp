#include <iostream>
using namespace std;

const int N = 1e5 + 5;
int arr[N];
int tmp[N];
long long count=0;

long long sort(int left, int right);
long long merge(int left, int mid, int right);

long long sort(int left, int right) {
    if (left == right) return 0;
    int mid = left + (right - left) / 2;
    long long leftPairs = sort(left, mid);
    long long rightPairs = sort(mid+1, right);
    long long crossPairs = merge(left, mid, right);
    return leftPairs + rightPairs + crossPairs;
}

long long merge(int left, int mid, int right) {
    int i = left, j = mid + 1, k = left;
    while(i <= mid && j <= right){
        if(arr[i] >= arr[j]){
            tmp[k++] = arr[j++];
            count += mid - i + 1;
        }else{
            tmp[k++] = arr[i++];
        }
    }
    while (i <= mid) tmp[k++] = arr[i++];
    while (j <= right) tmp[k++] = arr[j++];
    for (int l = left; l < right + 1; l++) arr[l] = tmp[l];
    return count;
}

int main() {
    int n;
    scanf("%d", & n); 
    for(int i = 0; i < n;i++) scanf("%d", & arr[i]);
    sort(0, n-1);
    printf("%lld", count);
    return 0;
}