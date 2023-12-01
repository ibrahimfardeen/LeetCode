class Solution:
    def reverseString(self, s: List[str]) -> None:
        x = s[::-1]
        for i in range(len(s)):
            s.pop(0)
        for i in x:
            s.append(i)
        """
        Do not return anything, modify s in-place instead.
        """
        
