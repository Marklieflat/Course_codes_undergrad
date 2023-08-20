class Node{
    int data;
    Node next;
    public Node(int data){
        this.data = data;
        this.next = null;
    }
}

class Queue{
    private static Node rear = null, front = null;
    public static int dequeue(){
        if (front == null){
            System.out.print("\nQueue Underflow");
            System.exit(1);
        }
        Node temp = front;
        System.out.printf("Removing %d\n", temp.data);
        front = front.next;
        if (front == null) rear = null;
        int item = temp.data;
        return item;
    }
    public static void enqueue(int item){
        Node node = new Node(item);
        System.out.printf("Inserting %d\n", item);
        if (front == null){
            front = node;
            rear = node;
        }
        else{
            rear.next = node;
            rear = node;
        }
    }
    public static int peek(){
        if (front != null) return front.data;
        else System.exit(1);
        return -1;
    }
    public static boolean isEmpty() {return rear == null && front == null;}
    
}

// class main{
//     public static void main(String[] args){
//         Queue q = new Queue();
//         q.enqueue(1);
//         q.enqueue(2);
//         q.enqueue(3);
//         q.enqueue(4);
//         System.out.printf("The front element is %d\n", q.peek());
//         q.dequeue();
//         q.dequeue();
//         q.dequeue();
//         q.dequeue();
//         if (q.isEmpty()) System.out.print("The queue is empty");
//         else System.out.print("The queue is not empty");
//     }
// }