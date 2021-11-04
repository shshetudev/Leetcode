public class RemoveElements {
    public static void main(String[] args) {
       System.out.println(removeElements(new int[] {0,1,2,2,3,0,4,2}, 2));
    }
    static int removeElements(int[] nums, int val){
        if(nums.length == 0) {
            return 0;
        }
        int validSize = 0;
        for (int i = 0; i < nums.length; i++) {
            if(nums[i] != val) {
                nums[validSize] = nums[i];
                validSize++;
            }
        }
        for (int i = 0; i < nums.length; i++) {
            System.out.print(nums[i] +" ");
        }
        return validSize;
    }
}