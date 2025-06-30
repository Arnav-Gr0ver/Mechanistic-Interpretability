#
# diff: med
# sol: brute force, figure out how to make optimal
#   time complex | O(n^2)
#   space complex | O(n)
#   time | 00:02:59.33
# 

class Solution:

    def encode(self, strs: List[str]) -> str:
        #combine strs with a delimiter
        out = ""
        for s in strs:
            out += s + '|'
        return out

    def decode(self, s: str) -> List[str]:
        #split string based on delimter
        l = []
        temp = ""
        for c in s:
            if c != '|':
                temp += c
            else:
                l.append(temp)
                temp = ""
        return l
        