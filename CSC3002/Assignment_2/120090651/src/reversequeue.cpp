/*
 * File: reversequeue.cpp
 * ----------------------
 * This file implements the reversequeue.h interface
 */


#include "reversequeue.h"
#include <iostream>
#include "stack.h"
using namespace std;
// TODO


void reverseQueue(Queue<string> & queue){
    Queue<string> newqueue = queue;
    Stack<string> stack;
    for (int i = 0; i < queue.size(); i++){
        stack.push(newqueue.dequeue());
    }
    queue.clear();
    while (!stack.isEmpty()){
        queue.enqueue(stack.pop());
    }
}

void listQueue(Queue<string> & queue){
    Queue<string> newqueue = queue;
    cout << "The queue contains: ";
    for (int i = 0; i < queue.size(); i++){
        cout << newqueue.dequeue() << " ";
    }
    cout << endl;
}
