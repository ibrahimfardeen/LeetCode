class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        index = 0
        if target in nums:
            return nums.index(target)
        else:
            return sorted(nums + [target]).index(target)
