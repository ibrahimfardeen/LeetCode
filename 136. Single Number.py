class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        x = sorted(nums)
        output = 0
        for i in range(0, len(x) - 1, 2):
            if (x[i] or x[i] == 0) and x[i+1] and x[i] != x[i+1]:
                return x[i]
            else:
                output = x[-1]
        return output
