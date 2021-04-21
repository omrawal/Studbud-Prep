import java.util.*;

class q1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n1 = sc.nextInt();
        int arr1[] = new int[n1];
        int i = 0;
        for (i = 0; i < n1; i++) {
            arr1[i] = sc.nextInt();
        }
        int n2 = sc.nextInt();
        int arr2[] = new int[n2];
        for (i = 0; i < n2; i++) {
            arr2[i] = sc.nextInt();
        }
        int union[] = new int[n1 + n2];
        int intersection[] = new int[n1 + n2];
        int arr1p = 0, arr2p = 0;
        int unionp = 0, interp = 0;
        while (arr1p < n1 && arr2p < n2) {
            if (arr1[arr1p] == arr2[arr2p]) {
                intersection[interp] = arr1[arr1p];
                union[unionp] = arr1[arr1p];
                unionp++;
                interp++;
                arr1p++;
                arr2p++;
            } else {
                if (arr1[arr1p] < arr2[arr2p]) {
                    union[unionp] = arr1[arr1p];
                    unionp++;
                    arr1p++;
                } else {
                    union[unionp] = arr2[arr2p];
                    unionp++;
                    arr2p++;
                }
            }

        }
        while (arr1p < n1) {
            union[unionp] = arr1[arr1p];
            unionp++;
            arr1p++;
        }
        while (arr2p < n2) {
            union[unionp] = arr2[arr2p];
            unionp++;
            arr2p++;
        }

        System.out.println("The Union is: ");
        for (i = 0; i < n1 + n2; i++) {
            System.out.print(union[i] + " ");
        }
        System.out.println();
        System.out.println("The Intersection is: ");
        for (i = 0; i < n1 + n2; i++) {
            System.out.print(intersection[i] + " ");
        }
    }
}