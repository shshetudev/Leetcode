from typing import List

# Time: O(n)
# Space: O(n)

class HashMapSoln(object): 
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i,num in enumerate(nums):
            complement = target - num
            if complement in map:
                return [map[complement],i]
            map[num] = i
        return []

if __name__ == "__main__":
    print(HashMapSoln().twoSum((2, 7, 11, 15), 9))                