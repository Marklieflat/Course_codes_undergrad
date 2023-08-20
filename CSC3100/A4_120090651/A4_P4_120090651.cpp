#include <string>
#include <iostream>
#include <cstdio>

using namespace std;

class Trie{
private:
    int count = 0;
    Trie* next[26] = {nullptr};
public:
    Trie(){}
    ~Trie(){}

    void insert(string word){
        Trie *node = this;
        for (char alpha : word){
            if (node->next[alpha - 'a'] == NULL) {
                node->next[alpha - 'a'] = new Trie();
            }
            node->next[alpha - 'a']->count++;
            node = node->next[alpha - 'a'];
        }
    }

    int numprefix(string pre){
        Trie *node = this;
        for (char alpha : pre){
            if (node->next[alpha - 'a'] != NULL){
                node = node->next[alpha - 'a'];
            }
            else return 0;
        }
        return node->count;
    }
};

inline string stringread(){
    string str;
    char s = getchar();
    while (s == '\n') s = getchar();
    while (s != '\n'){
        str += s;
        s = getchar();
    }
    return str;
}

int main(){
    Trie tree = Trie();
    int n;
    scanf("%d", &n);
    string str;
    while (n--){
        str = stringread();
        tree.insert(str);
    }
    int q;
    scanf("%d", &q);
    string search;
    while (q--){
        search = stringread();
        int count = tree.numprefix(search);
        printf("%d\n", count);
    }
    return 0;
}