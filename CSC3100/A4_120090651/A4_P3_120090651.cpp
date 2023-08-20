#include <iostream>
#include <cstdio>
#include <algorithm>

typedef long long ll;
using namespace std;
const int maxnode = 2005;
int n;
ll M;
int parent[maxnode*maxnode/2]; // Store its parent
ll ans = 0; // Store the answer
ll pop[maxnode]; // Store the popularity of each team

struct edge{
    int weight;
    int start;
    int end;
};

edge dist[maxnode*maxnode/2]; // Store the edge

ll getweight(ll ai, ll aj, ll M){ // Calculate the weight of each edge
    return (ai*aj) % M;
}

bool compare(const edge & x, const edge & y){ // Overload the compare condition
    return x.weight > y.weight;
}

int find(int x){ // Find its parent
    if (parent[x] == x) return x;
    return parent[x] = find(parent[x]);
}

void build(edge a){  // If parent are different, add the weight to the answer
    ans += a.weight;
    parent[find(a.start)] = parent[find(a.end)];
}

void Kruskal(int n){
    for (int i = 1; i <= n; i++){
        parent[i] = i; // Initialize the parent of each node
    }
    int numedge = 0;
    for (int i = 1; i <= n; i++){
        if (find(dist[i].start) == find(dist[i].end)){ // If their parents are the same, continue searching
            continue;
        }
        else{
            build(dist[i]); // Add the weight
            numedge++;
        }
        if (numedge == n-1) break; // If the edge is sufficient, stop
    }
}

int main(){
    scanf("%d%d", &n, &M);
    ll c;
    int cnt = 1;
    while (cin >> c){
        pop[cnt++] = c;
        char ch = getchar();
        if (ch == '\n') break;
    }
    int count = 0;
    for (int i = 1; i <= n; i++){
        for (int j = 1; j <= i; j++){
            if (i != j){
                dist[++count].start = i;
                dist[count].end = j;
                dist[count].weight = getweight(pop[i], pop[j], M);
            }
        }
    }
    sort(dist+1, dist+count+1, compare); // Sort the whole array
    Kruskal(count);
    printf("%lld", ans);
    return 0;
}