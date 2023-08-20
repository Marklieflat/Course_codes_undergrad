#include <stdio.h>
#include <queue>
#include <vector>
#include <cmath>
#include <iostream>
#include <algorithm>
using namespace std;

priority_queue <int, vector<int>, less<int> > maxheap;
priority_queue <int, vector<int>, greater<int> > minheap;
int medianarr[55];
int k;
int m;

void arrinsert(int arr[], int pos, int & count, int w){
    for (int i = count-1; i >= pos ; i--){
        arr[i+1] = arr[i];
    }
    arr[pos] = w;
    count++;
}

void arrdelete(int arr[], int pos, int & count){
    for (int i = pos; i < count; i++){
        arr[i] = arr[i+1];
    }
    count--;
}

void insertval(int arr[], int w, int & count){
    if (w < arr[0]) {
        maxheap.push(w);
        if (minheap.size() < maxheap.size()-1){
            minheap.push(arr[--count]);
            arrinsert(arr, 0, count, maxheap.top());
            maxheap.pop();
        }
        return;
    }
    if (w > arr[count-1]){
        minheap.push(w);
        if (minheap.size() > maxheap.size()){
            arr[count++] = minheap.top();
            minheap.pop();
            maxheap.push(arr[0]);
            arrdelete(arr, 0, count);
        }
        return;
    }
    for (int i = 0; i < count-1; i++){
        if (w > arr[i] && w < arr[i+1]){
            arrinsert(arr, i+1, count, w);
            if (maxheap.size() == minheap.size()){
                maxheap.push(arr[0]);
                arrdelete(arr, 0, count);
            }
            else{
                minheap.push(arr[--count]);
            }
            break;
        }
    }
}

void deleteval(int arr[], int p, int & count){
    arrdelete(arr, p-1, count);
    if (maxheap.size() == minheap.size()){
        arr[count++] = minheap.top();
        minheap.pop();
    }
    else{
        arrinsert(arr, 0, count, maxheap.top());
        maxheap.pop();
    }
}

void output(int arr[],  int count){
    for (int i = 0; i < count-1; i++) printf("%d ", arr[i]);
    printf("%d\n", arr[count-1]);
}

int main(){
	cin >> m >> k;
    int count = 0;
	for (int i = 0; i < 2*k; ++i) {
        cin >> medianarr[i];
        count++;
    }    
	sort(medianarr, medianarr + 2*k);
	while(m--){
		int op, w, p;
		cin >> op;
		if (op == 1){
			cin >> w;
			insertval(medianarr, w, count);
		}
		if (op == 2){
			output(medianarr, count);
		} 
		if (op == 3){
			cin >> p;
			deleteval(medianarr, p, count);
		}
	}
	return 0;
}