#
# diff: ez
# sol: optimal
#   time complex: O(n)
#   space complex: O(n)
# 

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #create a hash with freq of elements in nums
        #if any count >1 that's the duplicate

        hash_map = {}
        for n in nums:
            if n not in hash_map:
                hash_map[n] = 1 #counting all new
            else:
                return True #alr counted, that's the duplicate
        
        return False #no duplicates by time done counting