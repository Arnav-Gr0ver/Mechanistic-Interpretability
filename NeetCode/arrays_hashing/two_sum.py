#
# diff: ez
# sol:
#   time complex | O(n)
#   space complex | O(n)
#   time | 0:11:56.02
# 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #two unique elements that add up to target
        #for each #, find if it's complement exists in the remaining search space

        #go through each element
        #if complement exists, find its index

        #create a hash map of complements, with their index
        complement_map = {}
        for i in range(len(nums)):
            complement_map[nums[i]] = i
        
        for i in range(len(nums)):
            r = target - nums[i]
            if r in complement_map and complement_map[r] != i:
                l = [complement_map[r], i]
                l.sort()
                return l