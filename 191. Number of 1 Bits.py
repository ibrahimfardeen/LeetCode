class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        x = bin(n).replace("0b", "")
        for i in str(x):
            if i == '1':
                count += 1
        return count
