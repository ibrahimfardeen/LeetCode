class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        k = {}
        e = -99
        for i in list(set(nums)):
            count = 0
            for j in nums:
                if j == i:
                    count += 1
            e = max(e, count)
            k[count] = i
        return k[e]
