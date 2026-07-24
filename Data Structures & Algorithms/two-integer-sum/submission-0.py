class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       hash_set = {}
       n = len(nums)
       for i, num in enumerate(nums):
            difference = target - nums[i]
            if difference in hash_set:
                return [hash_set[difference], i]
            hash_set[num] = i
       return [] 
       
        