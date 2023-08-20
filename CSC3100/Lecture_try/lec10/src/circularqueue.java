import java.io.*;
class CircularQ {
    int Q[] = new int[100];
    int n, front, rear;
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    public CircularQ(int nn) {
        n = nn;
        front = rear = 0;
    }
    public void enqueue(int v) {
        if ((rear + 1) % n != front) {
            rear = (rear + 1) % n;
            Q[rear] = v;
        }
        else System.out.println("Queue is full!");
    }
    public int dequeue() {
        int v;
        if (front != rear) {
            front = (front + 1) % n;
            v = Q[front];
            return v;
        }
        else return -9999;
    }
    public void disp() {
        int i;
        if (front != rear) {
            i = (front + 1) % n;
            while (i != rear) {
                System.out.println(Q[i]);
                i = (i + 1) % n;
            }
        }
        else System.out.println("Queue is empty!");
    }
}

class test{
    public static void main(String[] args){
        CircularQ q = new CircularQ(10);
        q.enqueue(1);
        q.enqueue(2);
        q.enqueue(3);
        q.enqueue(4);
        q.disp();
        q.dequeue();
        q.disp();
        q.dequeue();
        q.dequeue();
        q.dequeue();
    }
}
