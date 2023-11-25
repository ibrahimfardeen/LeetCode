class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        charset = []
        a = len(nums)
        indexs = []
        for i in range(a):
            if nums[i] in charset:
                indexs.append(i)
            else:
                charset.append(nums[i])
        print(indexs)
        if indexs:
            for i in indexs[::-1]:
                print(i)
                nums.pop(i)
            print(nums)
        return len(nums)
