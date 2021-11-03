 # T.C.: O(n)
 # S.C.: O(1)
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        if len(nums) <2:
            return len(nums)
        pre = 0
        for cur in range(1,len(nums)):
            if(nums[cur]!=nums[pre]):
                pre+=1
                nums[pre]=nums[cur]
                
        return pre+1                
                
if __name__ == "__main__":
   print(Solution().removeDuplicates([1,2,3]))