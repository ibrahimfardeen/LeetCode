class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = ''
        temp = ''
        min_l = 0
        for i in strs:
            min_l = min(list(map(len, strs)))
        for i in range(min_l):
            if strs[0][i]:
                temp = strs[0][i]
            else:
                break
            for j in range(len(strs)):
                if strs[j][i] == temp:
                    temp = strs[j][i]
                    if j == (len(strs) - 1):
                        output += temp
                else:
                    return output
        return output
