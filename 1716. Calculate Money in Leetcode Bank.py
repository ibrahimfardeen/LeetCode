class Solution:
    def totalMoney(self, n: int) -> int:
        total = 0
        count = 0
        for j in range(1, ((n // 7) + 2)):
            for i in range(j, j+7):
                total += i
                count += 1
                if count == n:
                    return total
        return total
