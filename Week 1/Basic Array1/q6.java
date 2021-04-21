import java.util.*;

public class q6 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int k = sc.nextInt();
        int n = sc.nextInt();
        int i = 0;
        int[] arr = new int[n];
        for (i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        // System.out.println("The sorted array is: ");
        Arrays.sort(arr);
        int kthsmallest = 0;
        int kthlargest = 0;
        kthlargest = arr[n - k];

        kthsmallest = arr[k - 1];

        System.out.println("kthsmallest= " + kthsmallest);
        System.out.println("kthlargest= " + kthlargest);
        // for (i = 0; i < n; i++) {
        // System.out.print(arr[i] + " ");
        // }
        sc.close();
    }
}
