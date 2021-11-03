public class RemoveDuplicates1 {
    public static void main(String[] args) {
       System.out.println(removeDuplicates(new int[] {0,0,1,1,1,2,2,3,3,4}));
    }
    static int removeDuplicates(int[] nums){
        if(nums.length == 0) {
            return 0;
        }
        int value = nums[0];
        int lastIndex = 0;
        int count = 1;
        for (int i = 1; i < nums.length; i++) {
            if(nums[i] > value) {
                value = nums[i];
                lastIndex = lastIndex+1;
                nums[lastIndex] = value;
                count++;
            }
        }
        return count;
    }
}