import java.util.*;

public class q9 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int i = 0;
        int[] arr = new int[n];
        for (i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        int min_val = Integer.MAX_VALUE;
        int max_val = Integer.MIN_VALUE;
        for (i = 0; i < n; i++) {
            if (arr[i] < min_val) {
                min_val = arr[i];
            }
            if (arr[i] > max_val) {
                max_val = arr[i];
            }
        }
        int range = max_val - min_val;
        System.out.println("The range of given array is: " + range);
    }
}
