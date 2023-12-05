class Solution:
    def largestGoodInteger(self, num: str) -> str:
        a = 0
        zeroes = False
        for i in range(len(num) - 2):
            if num[i] == num[i+1] == num[i+2]:
                if num[i:i+3] == '000':
                    zeroes = True
                a = max(int(a), int(num[i:i+3]))
        if a == 0 and zeroes:
            return '000'
        elif a == 0 and zeroes == False:
            return ''
        return str(a)
