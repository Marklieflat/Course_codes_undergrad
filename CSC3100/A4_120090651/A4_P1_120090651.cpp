#include<cstdio>
#include<iostream>
#include<queue>
#include<stack>
#include<vector>
using namespace std;
const int maxedge = 2e5+5; // Maximum edge in the whole graph
const int maxnode = 1e5+5 + 2*maxedge; // Since we need to add two node on each edge, we need to increase node size by 2*maxedge
const int INF = 1e8;

struct Node{
    int v; // Store the next node
    int w; // Store the weight between the front one and next one
    Node(int endnode, int weight){
        v = endnode;
        w = weight;
    }
};

enum color{ // color of node used in dfs
    white = 0,
    gray = 1,
    black = 2
};

struct prnode{
    int idx; // index of the current node
    int length; // distance of each node to the root
    friend bool operator < (prnode a, prnode b) {
        return a.length > b.length;
    }
};

prnode dis[maxnode];
bool visit[maxnode]; // used in dijkstra
color check[maxnode]; // used in dfs
vector<Node> adj[maxnode]; // Store the graph
priority_queue<prnode> pq;

void addedge(int k){
    stack<int> Stack;
    int source = 1;
    Stack.push(source);
    check[source] = gray; // It has been included in the dfs path
    while (!Stack.empty()){
        int curr = Stack.top();
        bool unused = true;
        for (int i = 0; i < adj[curr].size(); i++){
            int frontnode = adj[curr][i].v;
            int frontweight = adj[curr][i].w;
            int mid = adj[frontnode][0].v; // Due to the data structure created, this node is at the middle of two edges
            for (int j = 0; j < adj[mid].size(); j++){
                int backnode = adj[mid][j].v;
                int backweight = adj[mid][j].w;
                if (backweight == k*frontweight && frontnode != backnode){ // add the node when the condition is satisfied
                    Node n = Node(backnode, (k-1)*frontweight);
                    adj[frontnode].push_back(n);
                }
            }
            if (!check[mid]){ // If the mid node hasn't been used, push the node into the heap
                unused = false;
                Stack.push(mid);
                check[mid] = gray;
                break;
            }
        }
        if (unused == true){ // If the node has been used, pop it out and color it
            check[curr] = black;
            Stack.pop();
        }
    }
}

void addnode(int from, int to, int & a, int w){ // add the undirectional edge
    a++;
    Node n1 = Node(a, w);
    adj[from].push_back(n1);
    Node n2 = Node(to, w);
    adj[a].push_back(n2);
    a++;
    Node n3 = Node(a, w);
    adj[to].push_back(n3);
    Node n4 = Node(from, w);
    adj[a].push_back(n4);
}

void initialize(int n){ // initialize the whole graph and distance array
    for (int i = 1; i <= n; i++){
        dis[i].length = INF;
        dis[i].idx = i;
        visit[i] = false;
        check[i] = white;
    }
}

void Dijkstra(int source, int K){
    dis[source].length = 0;
    pq.push(dis[source]);
    while(!pq.empty()){
        prnode leastnode = pq.top();
        pq.pop();
        int u = leastnode.idx;
        int len = leastnode.length;
        if (visit[u] == true) continue;
        visit[u] = true;
        int front = 0;
        while (front < adj[u].size()){
            int back = adj[u][front].v;
            int weight = adj[u][front].w;
            if (dis[back].length > len + weight){
                dis[back].length = len + weight;
                pq.push(dis[back]);
            }
            front++;
        }
    }
}

void output(int n){
    for (int end = 1; end <= n; end++){
        if (dis[end].length >= INF){
            printf("%d ", -1);
        }
        else{
            printf("%d ", dis[end].length / 2);
        }
    }
}

int main(){
    int n, m, K, u, v, w;
    scanf("%d%d%d", &n, &m, &K);
    int a = n;
    while(m--){
        scanf("%d%d%d", &u, &v, &w);
        addnode(u, v, a, w);
    }
    int s = 1;
    initialize(a);
    addedge(K);
    Dijkstra(s, K);
    output(n);
    return 0;
}