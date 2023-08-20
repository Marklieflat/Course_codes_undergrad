#include <iostream>
#include <string>
#include <stack>
#include <queue>
#include <stdio.h>
using namespace std;

bool check(queue<int> power);
string display(queue<int> q);
string display(string str);
queue<int> transfer(int n);
string recursion(queue<int> q);

bool check(queue<int> power) {
    bool flag = true;
    while (!power.empty()) {
        int i = power.front();
        if ((i != 0) && (i != 1) && (i != 2)) flag = false;
        power.pop();
    }
    return flag;
}

string display(queue<int> q) {
    string result = "";
    while (!q.empty()) {
        int i = q.front();
        if (i == 1) {
            result += "2";
            if (q.size() != 1) result += "+";
            q.pop();
            continue;
        }
        result = result + "2(" + to_string(i) + ")";
        if (q.size() != 1) result += "+";
        q.pop();
    }
    return result;
}

string display(string str) {
    if (str == "2(0)") return "2";
    if (str == "") return "2(0)";
    string result;
    result = result + "2(" + str + ")";
    return result;
}

queue<int> transfer(int n) {
    stack<int> binarystack;
    queue<int> power;
    while (n) {
        int temp = n % 2;
        binarystack.push(temp);
        n /= 2;
    }
    int size = binarystack.size();
    while (!binarystack.empty()) {
        if (binarystack.top()) {
            power.push(size-1);
        }
        binarystack.pop();
        size--;  
    }
    return power;
}

string recursion(queue<int> q) {
    string result = "";
    if (check(q)) return display(q);
    else{
        while (!q.empty()) {
            string str = recursion(transfer(q.front()));
            str = display(str);
            if (q.size() > 1) {
                result = result + str + "+";
            }
            else {
                result += str;
            }
            q.pop();
        }
    }
    return result;
}

int main() {
    int n;
    cin>>n;
    cout << recursion(transfer(n));
    cout<<endl;
    return 0;
}