import java.util.*;

public class q8 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int i = 0;
        int[] arr = new int[n];
        for (i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        int left, middle, right;
        int temp;
        left = 0;
        right = n - 1;
        middle = 0;
        while (middle <= right) {
            if (arr[middle] == 0) {
                temp = arr[middle];
                arr[middle] = arr[left];
                arr[left] = temp;
                left++;
                middle++;
            } else if (arr[middle] == 1) {
                middle++;
            } else if (arr[middle] == 2) {
                temp = arr[middle];
                arr[middle] = arr[right];
                arr[right] = temp;
                right--;
            }
        }
        System.out.println("Sorted array is: ");
        for (i = 0; i < n; i++) {
            System.out.print(arr[i] + " ");
        }
    }

}
