import java.util.*;

public class Fibonacci {
    static final int mod = 998244353;

    public static int getFibRec(int n){
        return additiveSequence(n, 1, 1);
    }

    public static int additiveSequence(int n, int t0, int t1){
        if (n == 0) return t0;
        if (n == 1) return t1;
        return additiveSequence(n - 1, t1 % mod, (t0 + t1) % mod);
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        input.close();
        int ans = getFibRec(n);
        System.out.println(ans);
    }
}