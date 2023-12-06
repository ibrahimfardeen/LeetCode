class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        a = t
        b = s
        for i in a:
            if i in b:
                a = a.replace(i, '', 1)
                b = b.replace(i, '', 1)
        return a
