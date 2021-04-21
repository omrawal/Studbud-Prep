public class q3 {
    public static void main(String[] args) {
        System.out.println("Missing Number!!");
    }

    int MissingNumber(int array[], int n) {
        // Your Code Here
        int expected_sum = (n * (n + 1)) / 2;
        int a_sum = 0, i = 0;
        for (i = 0; i < n - 1; i++) {
            a_sum += array[i];
        }
        return expected_sum - a_sum;

    }
}
