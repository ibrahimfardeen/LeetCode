class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = s.replace(' ','').lower()
        output = ''
        for i in x:
            if i.isalnum():
                output += i
        return output == output[::-1]
