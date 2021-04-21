import java.util.*;

public class q7 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int k = sc.nextInt();
        int n = sc.nextInt();
        int i = 0;
        int[] arr = new int[n];
        for (i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        int k_count = 0;
        for (i = 0; i < n; i++) {
            if (arr[i] == k) {
                k_count++;
            }
        }
        System.out.println("The occurance of " + k + " is " + k_count);
    }
}
