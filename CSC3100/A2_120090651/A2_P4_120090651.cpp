#include <iostream>
using namespace std;

static const int maxsize = 450;
int arrlen = 0;
int numoper;

struct Node {
    Node *next;
    int size;
    int array[2*maxsize + 5];
    long long sum;
    Node() {
        size = 0;
        next = NULL;
        sum = 0;
        for (int i = 0; i < 2*maxsize + 5; i++) {
            array[i] = 0;
        }
    }
    void push(int n) {
        array[size++] = n;
    } 
}* head = NULL;

void split(Node *p) {
    if (p->size >= 2*maxsize) {
        Node *q = new Node;
        long long psum = p->sum;
        for (int i = maxsize; i < p->size; i++) {
            q->push(p->array[i]);
            p->sum -= p->array[i];
        }
        q->sum = psum - p->sum;
        p->size = maxsize;
        q->next = p->next;
        p->next = q;
    }
}

void insert_element(int k, int x) {
    Node *p = head;
    int total; // Record the number of elements contained before the array that we want
    int count; // Index of the element in the array in the particular node
    if (k > arrlen++) {
        while (p->next != NULL) {
            p = p->next;
        }
        p->push(x);
        p->sum += x;
        split(p);
        return;
    }
    p = head;
    for (total = head->size; p != NULL && total < k; p = p->next, total += p->size);
    total -= p->size;
    count = k - total;
    for (int i = p->size - 1; i >= count; i--) p->array[i + 1] = p->array[i];
    p->array[count] = x;
    p->size++;
    p->sum += x;
    split(p);
}

void delete_element(int k) {
    Node *p = head;
    int total; // Record the number of elements contained before the array that we want
    int count; // Index of the element in the array in the particular node
    for (total = head->size; p != NULL && total < k; p = p->next, total += p->size);
    total -= p->size;
    count = k - total - 1;
    p->sum -= p->array[count];
    for (int i = count; i < p->size - 1; i++) p->array[i] = p->array[i+1];
    p->size--;
}

long long summation(int l, int r) {
    long long ans = 0;
    Node *pl = head;
    Node *pr = head;
    int total_l, count_l, total_r, count_r;
    for (total_l = head->size; pl != NULL && total_l < l; pl = pl->next, total_l += pl->size);
    total_l -= pl->size;
    count_l = l - total_l - 1;
    
    if (l == r) {
        ans += pl->array[count_l];
        return ans;
    }
    
    for (total_r = head->size; pr != NULL && total_r < r; pr = pr->next, total_r += pr->size);
    total_r -= pr->size;
    count_r = r - total_r - 1;

    if (pl == pr) {
        for (int i = count_l; i <= count_r; i++) ans += pl->array[i];
        return ans;
    }
    
    for (int i = count_l; i < pl->size; i++) {
        ans += pl->array[i];
    }
    pl = pl->next;
    while (pl != pr) {
        ans += pl->sum;
        pl = pl->next;
    }
    for (int j = 0; j <= count_r; j++) ans += pr->array[j];
    return ans;
}

void readch(char& ch) {
    do ch = getchar();
    while (!isdigit(ch));
}

int main() {
    scanf("%d", & numoper);
    Node *p = new Node;
    head = p;
    char a;
    int b,c;
    long long result;
    while (numoper--) {
        readch(a);
        if (a == '1') {
            arrlen++;
            scanf("%d %d", &b, &c);
            insert_element(b, c);
        }
        if (a == '2') {
            arrlen--;
            scanf("%d", &b);
            delete_element(b);
        }
        if (a == '3') {
            scanf("%d %d", &b, &c);
            result = summation(b, c);
            cout << result << endl;
        }
    }
}