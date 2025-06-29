#
# diff: med
# sol: kinda optimal
#   time complex | O(nlogn)
#   space complex | O(n)
#   time | 0:14:40.62 
# 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #find frequency of each unique element
        #return highest frequency elements, up to k times
        element_freq = {}
        for i in range(len(nums)):
            if nums[i] not in element_freq:
                element_freq[nums[i]] = 1
            else:
                element_freq[nums[i]] += 1
        
        #sorts hash by list of tuples then reverts
        sorted_hash = dict(sorted(element_freq.items(), key=lambda item: item[1]))
        
        final = []
        for i in range(k):
            final.append(sorted_hash.popitem()[0])
        
        return final