#
# diff: med
# sol: almost there
#   time complex | O(nlogn)
#   space complex | O(n)
#   time | 00:19:50.88
# 

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #remove duplicates
        #sort array
        m = nums.copy()
        m = set(m)
        m = list(m)
        m.sort()
        max_l = 0
        temp = 0
        
        if len(m) == 1:
            return 1

        for i in range(len(m)):
            if i == 0:
                temp += 1
            else:
                if m[i] - m[i-1] == 1:
                    temp += 1
                    if temp > max_l:
                        max_l = temp
                else:
                    temp = 1
        
        return max_l