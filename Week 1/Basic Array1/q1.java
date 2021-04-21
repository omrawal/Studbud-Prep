import java.util.*;

class q1 {
    public static void main(String[] args) {
        int arr[] = new int[10];
        int i = 0, n = 10;
        Scanner sc = new Scanner(System.in);
        for (i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        for (i = 0; i < n; i++) {
            System.out.println("_" + arr[i]);
        }
        sc.close();
    }
}