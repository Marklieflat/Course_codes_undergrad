public class inversion{
    public int reverse(int[] arr){
        if(arr.length < 2){
            return 0;
        }
        int[] copy=arr.clone();
        return reverse(copy, 0, arr.length-1);
    }

    public int reverse(int[] arr,int left,int right){
        if(left == right){
            return 0;
        }
        int mid = left + (right - left) / 2;
        int leftPairs = reverse(arr, left, mid);
        int rightPairs = reverse(arr, mid+1, right);
        int crossPairs = merge(arr, left, mid, right);
        return leftPairs + rightPairs + crossPairs;
    }

    public int merge(int[] arr, int left, int mid, int right){
        int[] tempArr = arr.clone();
        int i = left, j = mid + 1, k = left, count=0;
        while(i <= mid && j <= right){
            if(tempArr[i] >= tempArr[j]){
                arr[k] = tempArr[j];
                j++;
                k++;
                count += mid-i+1;
            }else{
                arr[k] = tempArr[i];
                i++;
                k++;
            }
        }
        if(i == mid+1){
            for(; k <= right; k++){
                arr[k] = tempArr[j];
            }
        }
        if(j == right+1){
            for(; k <= right; k++){
                arr[k] = tempArr[i];
            }
        }
        return count;
    }

    public static void main(String[] args){
        inversion sol = new inversion();
        int[] arr = {4,1,4,6,7,7,5};
        int finall = sol.reverse(arr);
        System.out.println("The number of inversion pairs: " + finall);
    }
}
