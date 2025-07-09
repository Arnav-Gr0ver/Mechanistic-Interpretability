#
# diff: med
# sol: optimal
#   time complex | O(n)
#   space complex | O(1)
#   time | 00:20:15.92
# 

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # any two bars to form container
        # container area is the height of the smaller bar of the 2, * the distance
        max_water = 0
        pointer1 = 0
        pointer2 = len(heights) - 1
        while pointer1 < pointer2:
            temp = min(heights[pointer1], heights[pointer2]) * (pointer2 - pointer1)
            if temp > max_water:
                max_water = temp
            if heights[pointer1] >= heights[pointer2]:
                pointer2 -= 1
            else:
                pointer1 += 1
        return max_water