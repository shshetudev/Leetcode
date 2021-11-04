 # T.C.: O(n)
 # S.C.: O(1)
from typing import List


class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeElements(self, nums: List[int], val: int) -> int:
        valid_size = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[valid_size] = nums[i]
                valid_size +=1
        return valid_size        
                
if __name__ == "__main__":
   print(Solution().removeElements([0,1,2,2,3,0,4,2],2))