class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        a = len(nums)
        indexs = []
        for i in range(a):
            if nums[i] == val:
                indexs.append(i)
        for i in indexs[::-1]:
            nums.pop(i)
        return len(nums)
