class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       for i,j in enumerate(nums):
           for k,l in enumerate(nums):
               if j+l == target and i != k:
                   return [i, k]
