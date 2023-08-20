/*
 * File: TraverseTest.cpp
 * ------------------
 * This program reimplements the depth-first search algorithm using an
 * explicit stack
 * or
 * reimplements the breadth-first search algorithm using an
 * explicit queue.
 */

#include "P2Traverse.h"

using namespace std;

void dfs(Node *start){
    Set<Node *> visited;
    Stack<Node *> notvisit;
    notvisit.push(start);
    while (!notvisit.isEmpty()){
        start = notvisit.pop();
        if (!visited.contains(start)){
            cout << start->name << endl;
            visited.add(start);
            for (Arc* arc : start->arcs){
               if (!visited.contains(arc->finish)){
                   notvisit.push(arc->finish);
               }
            }
        }
    }
}

void bfs(Node *start){
    Set<Node *> visited;
    Queue<Node *> notvisit;
    notvisit.enqueue(start);
    while (!notvisit.isEmpty()){
        start = notvisit.dequeue();
        if (!visited.contains(start)){
            cout << start->name << endl;
            visited.add(start);
            for (Arc *arc : start->arcs){
                if (!visited.contains(arc->finish)){
                    notvisit.enqueue(arc->finish);
                }
            }
        }
    }
}
