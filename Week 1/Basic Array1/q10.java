import java.util.*;

public class q10 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int i = 0;
        int[] arr = new int[n];
        for (i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        int left = 0;
        int current = 0, temp = 0;
        while (current < n && left < n) {
            if (arr[current] < 0) {
                temp = arr[left];
                arr[left] = arr[current];
                arr[current] = temp;
                left++;
                current++;
            } else
                current++;
        }
        System.out.println("Modified array is: ");
        for (i = 0; i < n; i++) {
            System.out.print(arr[i] + " ");
        }

    }
}
