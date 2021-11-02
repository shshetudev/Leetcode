
public class TraverseEachElement {
    public static void main(String[] args) {
        System.out.println("Hello World");
        System.out.println(twoSum(new int[] {2,7,11,15},9));
    }

    public static int[] twoSum(int[] nums, int target){
        for (int i = 0; i < nums.length-1; i++) {
            for (int j = 0; j < nums.length; j++) {
                if(nums[i]+nums[j] == target) {
                    return new int[] {i,j};
                }
            }
        }
        throw new IllegalArgumentException("No two sum solution");
    }
}