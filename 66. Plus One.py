class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        x = ''
        for i in digits:
            x += str(i)
        y = int(x) + 1
        b = []
        for i in str(y):
            b.append(int(i))
        return b
