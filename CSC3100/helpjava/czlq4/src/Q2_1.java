import java.util.*;
public class Q2_1{
    int k;
    static class MinHeap{
        PriorityQueue<Integer> array = new PriorityQueue<>((i1, i2) -> i1 - i2);
    }
    static class MaxHeap {
        PriorityQueue<Integer> array = new PriorityQueue<>((i1, i2) -> i2 - i1);
    }
    class medianList{
        int[] mList;
        int size;
        medianList(int k){
            size = 2*k;
            mList = new int[size];
        }
    }
    MinHeap MH_min;
    MaxHeap MH_max;
    medianList meList;

    void constructHeap(int[] arr){
        MH_min = new MinHeap();
        MH_max = new MaxHeap();
        meList = new medianList(k);
        int i =0;
        for (int ele : arr) {
            meList.mList[i++] = ele;
        }
    }
    public boolean sizeIsOdd;
    void insert(int key){
        if (sizeIsOdd) {
            if (key < meList.mList[0]) {
                MH_max.array.add(key);
                int a = MH_max.array.poll();
                int b = meList.mList[2 * k - 1];
                meList.mList[2 * k - 1] = a;
                Arrays.sort(meList.mList);
                MH_min.array.add(b);
            } else if (key > meList.mList[0] && key < meList.mList[2 * k - 1]) {
                int b = meList.mList[2 * k - 1];
                meList.mList[2 * k - 1] = key;
                Arrays.sort(meList.mList);
                MH_min.array.add(b);
            } else {
                MH_min.array.add(key);
            }
            sizeIsOdd = false;
        }
        else {
            if (key > meList.mList[2*k-1]) {
                MH_min.array.add(key);
                int a = MH_min.array.poll();
                int b = meList.mList[0];
                meList.mList[0] = a;
                Arrays.sort(meList.mList);
                MH_max.array.add(b);
            } else if (key > meList.mList[0] && key < meList.mList[2 * k - 1]) {
                int b = meList.mList[0];
                meList.mList[0] = key;
                Arrays.sort(meList.mList);
                MH_max.array.add(b);
            } else {
                MH_max.array.add(key);
            }
            sizeIsOdd = true;
        }
    }
    void delete(int p){
        int a;
        if (sizeIsOdd) {
            a = MH_max.array.poll();
            sizeIsOdd = false;
        } else{
            a = MH_min.array.poll();
            sizeIsOdd = true;
        }
        meList.mList[p - 1] = a;
        Arrays.sort(meList.mList);
    }
    void printMedian(){
        for (int t =0; t<2*k;t++){
            if (t != 2*k-1) System.out.print(meList.mList[t]+" ");
            else {
                System.out.print(meList.mList[t]);
                System.out.println();
            }
        }
    }

    public static void main(String[] args) {
        Q2_1 heap = new Q2_1();
        Scanner scan = new Scanner(System.in);
        int m = scan.nextInt();
        int k = scan.nextInt();
        heap.k = k;

        int[] arr = new int[2*k];

        int t=0;
        while (t<2*k){
            int input = scan.nextInt();
            arr[t] = input;
            t++;
        }
        Arrays.sort(arr);
        heap.constructHeap(arr);
        int j = 0;
        while(j < m) {
            int type_operation = scan.nextInt();
            //1 w: insert a value w.
            if (type_operation == 1) {heap.insert(scan.nextInt());}
            //2: output all the median 2k values
            else if (type_operation == 2) {heap.printMedian();}
            //3 p: delete the p-th value among median 2k values, i.e. a (t-k+p).
            else heap.delete(scan.nextInt());
            j++;
        }
    }
}