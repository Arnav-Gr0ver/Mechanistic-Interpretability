#BRUTE FORCE
#3 min pause
#ADD optimal solution when completed

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #go through array, and for each element product everything else
        new = []
        temp = 1
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    temp *= nums[j]
            new.append(temp)
            temp = 1
        return new