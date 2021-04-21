import java.util.*;

public class q5 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int i = 0;
        int[] arr = new int[n];
        for (i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        System.out.println("The sorted array is: ");
        Arrays.sort(arr);
        for (i = 0; i < n; i++) {
            System.out.print(arr[i] + " ");
        }
        sc.close();
    }
}
