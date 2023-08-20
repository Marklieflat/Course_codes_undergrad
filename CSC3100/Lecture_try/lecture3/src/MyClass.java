import java.util.*;

// public class MyClass {
//     public int x, y;

//     public MyClass(int a, int b){
//         x = a;
//         y = b;
//     }
//     public static void swap(MyClass obj_a, MyClass obj_b){
//         MyClass tmp = obj_a;
//         obj_a = obj_b;
//         obj_b = tmp;

//         System.out.println("# obj_a: x=" + obj_a.x + " y=" + obj_a.y);
//         System.out.println("# obj_a: x=" + obj_b.x + " y=" + obj_b.y);
//         System.out.println();
//     }
//     public static void main(String[] args){
//         MyClass obj_1 = new MyClass(1, 2);
//         MyClass obj_2 = new MyClass(10, 20);

//         MyClass.swap(obj_1, obj_2);

//         System.out.println("# obj1: x=" + obj_1.x + " y=" + obj_1.y);
//         System.out.println("# obj2: x=" + obj_2.x + " y=" + obj_2.y);
//     }
// }

// public class MyClass {
//     public int x, y;

//     public MyClass(int a, int b){
//         x = a;
//         y = b;
//     }
//     public static void swap(MyClass obj_a, MyClass obj_b){
//         int tmp = obj_a.x;
//         obj_a.x = obj_b.x;
//         obj_b.x = tmp;

//         tmp = obj_a.y;
//         obj_a.y = obj_b.y;
//         obj_b.y = tmp;

//         System.out.println("# obj_a: x=" + obj_a.x + " y=" + obj_a.y);
//         System.out.println("# obj_a: x=" + obj_b.x + " y=" + obj_b.y);
//         System.out.println();
//     }
//     public static void main(String[] args){
//         MyClass obj_1 = new MyClass(1, 2);
//         MyClass obj_2 = new MyClass(10, 20);

//         MyClass.swap(obj_1, obj_2);

//         System.out.println("# obj1: x=" + obj_1.x + " y=" + obj_1.y);
//         System.out.println("# obj2: x=" + obj_2.x + " y=" + obj_2.y);
//     }
// }
public class MyClass {
    public static void main(String[] args){
        StringBuffer sb = new StringBuffer("Hello ");
        System.out.println("before change, sb is " + sb.toString());
        change(sb);
        System.out.println("after change, sb is " + sb.toString());
    }
    public static void change(StringBuffer stringbuffer){
        stringbuffer = new StringBuffer("Hi ");
        stringbuffer.append("world !");
    }
}