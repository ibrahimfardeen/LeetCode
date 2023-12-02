class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = 0
        for i in words:
            a = chars
            x = 0
            for j in i:
                if j in a:
                    a = a.replace(j, '',1)
                    x += 1
            if len(i) == x:
                count += len(i)
        return count
