import java.util.*;

public class q10 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int arr[] = new int[n];
        int i = 0;
        for (i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        int max1 = Integer.MIN_VALUE, max2 = Integer.MIN_VALUE, max3 = Integer.MIN_VALUE;
        for (i = 0; i < n; i++) {
            if (arr[i] > max1) {
                max3 = max2;
                max2 = max1;
                max1 = arr[i];
            } else if (arr[i] > max2) {
                max3 = max2;
                max2 = arr[i];
            } else if (arr[i] > max3) {
                max3 = arr[i];
            }
        }
        System.out.println("max= " + max1 + " 2nd max= " + max2 + " 3rd max= " + max3);

    }
}
