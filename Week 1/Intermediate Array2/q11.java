public class q11 {

    public static void alternate(int arr[]) {
        int n = arr.length;
        int i = 1, curr = 1, temp = 0, flag = 0;
        // assuming 0 as positive
        while (curr < n) {
            if (arr[curr - 1] > -1) {
                flag = 1;
                for (i = curr + 1; i < n; i++) {
                    if (arr[i] < 0) {
                        temp = arr[i];
                        arr[i] = arr[curr];
                        arr[curr] = temp;

                        break;
                    }
                }
                curr++;
                // return;
            } else {
                flag = -1;
                for (i = curr + 1; i < n; i++) {
                    if (arr[i] > -1) {
                        temp = arr[i];
                        arr[i] = arr[curr];
                        arr[curr] = temp;

                        break;
                    }
                }
                curr++;
                // return;
            }

        }
    }

    public static void main(String[] args) {
        int arr[] = { -5, -2, 5, 2, 4, 7, 1, 8, 0, -8 };
        int n = arr.length;
        int i = 1;
        alternate(arr);
        for (i = 0; i < n; i++) {
            System.out.print(" " + arr[i]);
        }
    }
}
