public class MergeSort {
    public static void mergeSort(int[] items) {
        int[] temp = new int[items.length];
        sort(items, temp, 0, items.length - 1);
    }

    private static void sort(int[] items, int[] temp, int left, int right) {
        if (left < right) {
            int middle = (left + right) / 2;
            sort(items, temp, left, middle);
            sort(items, temp, middle + 1, right);
            merge(items, temp, left, middle, right);
        }
    }

    private static void merge(int items[], int[] temp, int left, int middle, int right) {
        int leftPos = left;
        int leftEnd = middle;
        int rightPos = middle + 1;
        int rightEnd = right;
        int tempPos = left;
        // Both sub-arrays have elements left over
        while (leftPos <= leftEnd && rightPos <= rightEnd) {
            if (items[leftPos] <= items[rightPos]) {
                temp[tempPos] = items[leftPos];
                leftPos++;
            } else {
                temp[tempPos] = items[rightPos];
                rightPos++;
            }
            tempPos++;
        }
        // The left subarray has elements left over
        while (leftPos <= leftEnd) {
            temp[tempPos] = items[leftPos];
            leftPos++;
            tempPos++;
        }
        // The right subarray has elements left over
        while (rightPos <= rightEnd) {
            temp[tempPos] = items[rightPos];
            rightPos++;
            tempPos++;
        }
        // Copy the sorted array to the original array
        for (int i = left; i <= right; i++)
            items[i] = temp[i];
    }
}
